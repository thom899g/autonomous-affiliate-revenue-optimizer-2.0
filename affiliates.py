import logging
from data_connectors import GoogleAnalyticsConnector
from ml_models import AffiliatesMLModel
from config import CONFIG

class AffiliateRevenueOptimizer:
    def __init__(self):
        self.data_connector = GoogleAnalyticsConnector()
        self.ml_model = AffiliatesMLModel()
        self.logger = logging.getLogger(__name__)

    def run(self):
        try:
            # 1. Pull data from GA
            data = self.data_connector.fetch_affiliate_data(CONFIG['GA_PROFILE_ID'])
            
            if not data:
                self.logger.warning("No data retrieved from Google Analytics.")
                return
                
            # 2. Process and predict high-converting offers
            predictions = self.ml_model.predict_high_converting_offers(data)
            
            # 3. Execute the optimal offer strategy
            self.execute_strategy(predictions)
            
            self.logger.info("Affiliate revenue optimization completed successfully.")

        except Exception as e:
            self.logger.error(f"Critical error during affiliate optimization: {str(e)}", exc_info=True)
            raise

    def execute_strategy(self, predictions):
        """Executes the optimized strategy based on model predictions."""
        try:
            # Example actions: update offers in the system, notify dashboard
            if predictions:
                self.logger.info(f"Executing strategy for top offer: {predictions[0]}")
                # Integration with other systems here
                DashboardNotifier(CONFIG['DASH_API_KEY']).update_offer_predictions(predictions)
        except Exception as e:
            self.logger.error(f"Failed to execute strategy: {str(e)}", exc_info=True)