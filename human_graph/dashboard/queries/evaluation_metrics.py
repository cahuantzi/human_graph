class EvaluationMetrics:

    def __init__(self, evaluation_repository):
        self.evaluation_repository = evaluation_repository

    def get_evaluation_metrics(self, evaluation_id):
        return {'waterPercen': 10}