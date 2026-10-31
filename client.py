# -*- coding: utf-8 -*-
"""
Personal Agent Dunbar Relationship Cadence Client
Zero-dependency Dunbar concentric layer social network classifier,
exponential relationship half-life decay estimator, and thoughtful touchpoint scheduler.
"""

import math
from typing import Dict, List, Any, Optional

class PersonalAgentDunbarRelationshipCadence:
    """
    Maintains personal social capital using Dunbar's concentric circle topology.
    Models interaction warmth decay and schedules intentional reconnection touchpoints.
    """

    DUNBAR_LAYERS = {
        "SUPPORT_CLIQUE": {"max_size": 5, "target_cadence_days": 7, "half_life_days": 14.0},
        "SYMPATHY_GROUP": {"max_size": 15, "target_cadence_days": 21, "half_life_days": 45.0},
        "AFFINITY_NETWORK": {"max_size": 50, "target_cadence_days": 60, "half_life_days": 90.0},
        "ACTIVE_ACQUAINTANCES": {"max_size": 150, "target_cadence_days": 180, "half_life_days": 240.0}
    }

    def classify_dunbar_layer_and_cadence(
        self,
        contact_id: str,
        closeness_score: float,
        days_since_last_contact: int
    ) -> Dict[str, Any]:
        """
        Classifies contact into Dunbar circle and evaluates interaction decay.
        Warmth(t) = exp(-ln(2) * t / HalfLife)
        """
        score = max(0.0, min(1.0, closeness_score))
        days = max(0, int(days_since_last_contact))

        if score >= 0.85:
            layer = "SUPPORT_CLIQUE"
        elif score >= 0.65:
            layer = "SYMPATHY_GROUP"
        elif score >= 0.40:
            layer = "AFFINITY_NETWORK"
        else:
            layer = "ACTIVE_ACQUAINTANCES"

        cfg = self.DUNBAR_LAYERS[layer]
        half_life = cfg["half_life_days"]
        target_cadence = cfg["target_cadence_days"]

        # Exponential relationship warmth decay
        warmth = round(math.exp(-math.log(2.0) * days / half_life), 3)
        drift_risk = round(1.0 - warmth, 3)
        days_overdue = max(0, days - target_cadence)

        if days_overdue > 0 and drift_risk >= 0.40:
            action = "PROACTIVE_TOUCHPOINT_URGENT"
        elif days_overdue > 0:
            action = "UPCOMING_TOUCHPOINT_GENTLE"
        else:
            action = "RELATIONSHIP_HEALTHY"

        return {
            "contact_id": contact_id,
            "closeness_score": score,
            "dunbar_layer": layer,
            "days_since_last_contact": days,
            "target_cadence_days": target_cadence,
            "days_overdue": days_overdue,
            "relationship_warmth_level": warmth,
            "drift_risk_score": drift_risk,
            "touchpoint_recommendation": action
        }

    def compute_relationship_entropy_and_drift(
        self,
        contacts_history: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Audits health of overall personal social network across all Dunbar layers.
        """
        if not contacts_history:
            raise ValueError("Contacts history list cannot be empty.")

        layer_counts = {"SUPPORT_CLIQUE": 0, "SYMPATHY_GROUP": 0, "AFFINITY_NETWORK": 0, "ACTIVE_ACQUAINTANCES": 0}
        overdue_contacts = []
        warmth_sum = 0.0

        for c in contacts_history:
            cid = c.get("id", "c_unknown")
            score = float(c.get("closeness_score", 0.5))
            days = int(c.get("days_since_last_contact", 10))

            res = self.classify_dunbar_layer_and_cadence(cid, score, days)
            layer_counts[res["dunbar_layer"]] += 1
            warmth_sum += res["relationship_warmth_level"]

            if res["days_overdue"] > 0:
                overdue_contacts.append({
                    "id": cid,
                    "layer": res["dunbar_layer"],
                    "days_overdue": res["days_overdue"],
                    "drift_risk": res["drift_risk_score"]
                })

        # Sort overdue contacts by drift risk descending
        overdue_contacts.sort(key=lambda x: x["drift_risk"], reverse=True)
        mean_warmth = round(warmth_sum / len(contacts_history), 3)

        return {
            "total_contacts_monitored": len(contacts_history),
            "layer_distribution": layer_counts,
            "average_network_warmth": mean_warmth,
            "total_overdue_touchpoints": len(overdue_contacts),
            "top_priority_reconnections": overdue_contacts[:5],
            "social_network_status": "HIGHLY_ENGAGED" if mean_warmth >= 0.70 else ("MODERATE_DRIFT" if mean_warmth >= 0.45 else "SEVERE_SOCIAL_ISOLATION_RISK")
        }

    def generate_thoughtful_reconnection_cadence(
        self,
        contacts: List[Dict[str, Any]],
        weekly_touchpoint_budget: int = 5
    ) -> Dict[str, Any]:
        """
        Schedules high-priority reconnections within weekly personal cognitive budget.
        """
        audit = self.compute_relationship_entropy_and_drift(contacts)
        top_candidates = audit["top_priority_reconnections"][:weekly_touchpoint_budget]

        scheduled = []
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        for idx, item in enumerate(top_candidates):
            day = days_of_week[idx % len(days_of_week)]
            scheduled.append({
                "contact_id": item["id"],
                "scheduled_day": day,
                "layer": item["layer"],
                "drift_risk": item["drift_risk"],
                "interaction_style": "Personal voice call / in-person coffee" if item["layer"] == "SUPPORT_CLIQUE" else "Thoughtful async text or article share"
            })

        return {
            "weekly_budget": weekly_touchpoint_budget,
            "scheduled_touchpoints_count": len(scheduled),
            "cadence_schedule": scheduled,
            "personal_agent_note": "Reconnections scheduled with zero social pressure; formatted as authentic personal touchpoints."
        }
