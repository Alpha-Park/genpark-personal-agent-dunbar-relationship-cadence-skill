# -*- coding: utf-8 -*-
import json
from client import PersonalAgentDunbarRelationshipCadence

cadence = PersonalAgentDunbarRelationshipCadence()

print("=" * 64)
print("DEMO: Personal Dunbar Relationship Cadence & Social Capital")
print("=" * 64)

# 1. Single contact classification
c1 = cadence.classify_dunbar_layer_and_cadence(contact_id="bob_closest_friend", closeness_score=0.92, days_since_last_contact=18)
print(f"\n1. Close Contact Audit ({c1['contact_id']}):")
print(f"   Dunbar Layer: {c1['dunbar_layer']} (Warmth: {c1['relationship_warmth_level']} | Drift: {c1['drift_risk_score']})")
print(f"   Days Overdue: {c1['days_overdue']} -> Recommendation: {c1['touchpoint_recommendation']}")

# 2. Network-wide audit
network = [
    {"id": "mom", "closeness_score": 0.98, "days_since_last_contact": 4},
    {"id": "mentor_david", "closeness_score": 0.75, "days_since_last_contact": 35},
    {"id": "college_roommate", "closeness_score": 0.88, "days_since_last_contact": 28},
    {"id": "former_colleague_sarah", "closeness_score": 0.50, "days_since_last_contact": 95},
    {"id": "hiking_buddy_mark", "closeness_score": 0.70, "days_since_last_contact": 14}
]

audit = cadence.compute_relationship_entropy_and_drift(network)
print(f"\n2. Network-Wide Social Capital Audit:")
print(f"   Monitored: {audit['total_contacts_monitored']} contacts (Avg Warmth: {audit['average_network_warmth']})")
print(f"   Distribution: {audit['layer_distribution']}")
print(f"   Overdue Reconnections: {audit['total_overdue_touchpoints']}")

# 3. Schedule thoughtful weekly reconnections
schedule = cadence.generate_thoughtful_reconnection_cadence(network, weekly_touchpoint_budget=3)
print(f"\n3. Weekly Mindful Touchpoint Schedule:")
for item in schedule["cadence_schedule"]:
    print(f"   [{item['scheduled_day']}] Reach out to {item['contact_id']} ({item['layer']}) -> {item['interaction_style']}")
