from app.service.analysis_service import AnalysisService

if __name__ == "__main__":
    analysis_service = AnalysisService()
    analysis_service.perform_analysis('BTCUSDT')
