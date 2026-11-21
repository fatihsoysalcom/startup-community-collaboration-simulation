import random

class Entrepreneur:
    """Represents an entrepreneur with a specific challenge or idea."""
    def __init__(self, name, challenge):
        self.name = name
        self.challenge = challenge

class CommunityMember:
    """Represents a community member or mentor with specific expertise."""
    def __init__(self, name, expertise):
        self.name = name
        self.expertise = expertise

    def offer_advice(self, challenge):
        """Provides advice based on their expertise, simulating community support."""
        # This section illustrates how different community members offer diverse perspectives
        # and solutions, a key benefit highlighted in the article.
        if self.expertise == "Funding":
            return f"{self.name} (Funding Expert): For '{challenge}', have you explored angel investors or grants?"
        elif self.expertise == "Marketing":
            return f"{self.name} (Marketing Guru): To tackle '{challenge}', consider a strong content strategy and targeted outreach."
        elif self.expertise == "Tech":
            return f"{self.name} (Tech Lead): What's your current tech stack for '{challenge}'? We might find an efficient solution."
        elif self.expertise == "Motivation":
            # This directly reflects the article's point about motivation and support.
            return f"{self.name} (Mentor): Don't give up on '{challenge}'! Every entrepreneur faces similar hurdles. Keep pushing!"
        elif self.expertise == "Strategy":
            return f"{self.name} (Strategist): Let's refine your approach to '{challenge}' by analyzing market trends."
        else:
            return f"{self.name} (General Support): That's a tough one, '{challenge}'. Let's brainstorm together."

def simulate_startup_cafe_session(entrepreneurs, community_members):
    """Simulates a session where entrepreneurs share and receive community feedback."""
    print("--- Welcome to The Startup Cafe Session! ---")
    print("Entrepreneurs share their challenges, and the community offers support.\n")

    for entrepreneur in entrepreneurs:
        # This step represents an entrepreneur sharing their ideas/problems (fikirlerinizi paylaşabileceğiniz).
        print(f"Entrepreneur {entrepreneur.name} shares: \"My current challenge is {entrepreneur.challenge}.\"")
        print("Community members respond:")

        # Simulate multiple community members offering diverse perspectives and support.
        # This demonstrates 'bilgi ve deneyimlerini paylaştığı' (sharing knowledge and experience)
        # and 'farklı perspektiflerden çözümler bulmanıza yardımcı olabilir' (helps find solutions from different perspectives).
        responders = random.sample(community_members, min(3, len(community_members)))
        for member in responders:
            print(f"  - {member.offer_advice(entrepreneur.challenge)}")
        print("-" * 60 + "\n")

# --- Setup the community: Entrepreneurs and Mentors ---
# Entrepreneurs facing various challenges, seeking community support.
entrepreneurs_list = [
    Entrepreneur("Ayşe", "finding initial seed funding"),
    Entrepreneur("Burak", "acquiring first 100 users"),
    Entrepreneur("Cem", "building a scalable backend infrastructure"),
    Entrepreneur("Deniz", "defining our unique value proposition"),
    Entrepreneur("Elif", "staying motivated during slow periods")
]

# Community members with different areas of expertise, ready to help.
community_members_list = [
    CommunityMember("Mentor Mert", "Motivation"),
    CommunityMember("Yatırımcı Yağmur", "Funding"),
    CommunityMember("Pazarlama Pınar", "Marketing"),
    CommunityMember("Geliştirici Gökhan", "Tech"),
    CommunityMember("Stratejist Selin", "Strategy"),
    CommunityMember("Büyüme Barış", "Marketing")
]

# Run the simulation of a Startup Cafe session.
if __name__ == "__main__":
    simulate_startup_cafe_session(entrepreneurs_list, community_members_list)
