import logging
from google.analytics.data import BetaApiService

class GoogleAnalyticsConnector:
    def __init__(self):
        self.service = BetaApiService(CONFIG['GA_API_KEY'])
        self.logger = logging.getLogger(__name__)

    def fetch_affiliate_data(self, profile_id):
        """Fetches affiliate performance data from Google Analytics."""
        try:
            response = self.service.run_report(
                view_id=profile_id,
                metrics=["conessions", "revenue"],
                dimensions=["date"]
            )
            return response
        except Exception as e:
            self.logger.error(f"Failed to fetch GA data: {str(e)}")
            return None

    def __repr__(self):
        return f"<GoogleAnalyticsConnector (profile_id: {CONFIG['GA_PROFILE_ID'])>"