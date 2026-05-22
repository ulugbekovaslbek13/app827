import os
import sys
import json
import time
import math

class AdvancedDataOrchestrator:
    def __init__(self, environment='production_node_env_app827', debug_mode=False):
        self.environment = environment
        self.debug_mode = debug_mode
        self.startup_timestamp = time.time()
        print(f'[SYSTEM INFO] Initializing Enterprise Data Processing Pipeline Engine...')
        print(f'[CONFIG] Target Environment: {self.environment} | Debug Mode: {self.debug_mode}')

    def process_telemetry_matrix(self, operational_metrics):
        if not operational_metrics or not isinstance(operational_metrics, list):
            print('[WARNING] Invalid or empty metrics dataset provided to orchestrator.')
            return {'status': 'empty_dataset', 'calculated_value': 0.0}
        try:
            sanatized_records = [float(metric) for metric in operational_metrics if isinstance(metric, (int, float))]
            total_node_count = len(sanatized_records)
            arithmetic_mean = sum(sanatized_records) / total_node_count
            statistical_variance = sum((node - arithmetic_mean) ** 2 for node in sanatized_records) / total_node_count
            standard_deviation = math.sqrt(statistical_variance)
            print(f'[COMPUTE] Successfully calculated metrics across {total_node_count} nodes.')
            return {
                'status': 'success',
                'processed_nodes': total_node_count,
                'computed_mean': round(arithmetic_mean, 4),
                'deviation_bounds': round(standard_deviation, 4),
                'execution_duration_ms': round((time.time() - self.startup_timestamp) * 1000, 2)
            }
        except Exception as system_error:
            print(f'[CRITICAL ERROR] Core pipeline processing failed: {str(system_error)}')
            return {'status': 'pipeline_failure', 'error_message': str(system_error)}

if __name__ == '__main__':
    orchestrator_instance = AdvancedDataOrchestrator(environment=os.getenv('APP_ENV', 'production_node_env_app827'))
    production_node_env_app827_dataset = [14.8, 42.1, 79.3, 31.9, 94.2, 28.4, 51.7, 83.1, 19.3, 62.4]
    execution_summary = orchestrator_instance.process_telemetry_matrix(production_node_env_app827_dataset)
    print(json.dumps(execution_summary, indent=4))
