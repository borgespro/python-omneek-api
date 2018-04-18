import json
import requests


class OmneekApi:
    def __init__(self, url, token):
        self.url = url
        self.token = token

    def _make_request(self, method_name, **kwargs):
        pass

    # Documents Management Methods

    def learn(self):
        # ToDo: Implement this method.
        pass

    def learn_url(self):
        # ToDo: Implement this method.
        pass

    def add_document(self):
        # ToDo: Implement this method.
        pass

    def add_text(self):
        # ToDo: Implement this method.
        pass

    def list_documents(self):
        # ToDo: Implement this method.
        pass

    def document_by_origin(self):
        # ToDo: Implement this method.
        pass

    def move_document(self):
        # ToDo: Implement this method.
        pass

    def delete_document(self):
        # ToDo: Implement this method.
        pass

    # Groups Management Methods

    def list_documents_in_group(self):
        # ToDo: Implement this method.
        pass

    def get_group_id(self):
        # ToDo: Implement this method.
        pass

    def move_group(self):
        # ToDo: Implement this method.
        pass

    def new_group(self):
        # ToDo: Implement this method.
        pass

    def delete_group(self):
        # ToDo: Implement this method.
        pass

    def delete_all(self):
        # ToDo: Implement this method.
        pass

    def total_documents(self):
        # ToDo: Implement this method.
        pass

    # Text Methods

    def get_phrase_text(self):
        # ToDo: Implement this method.
        pass

    def get_piece_text(self):
        # ToDo: Implement this method.
        pass

    def get_full_text(self):
        # ToDo: Implement this method.
        pass

    # Searches Methods

    def search_for_phrase(self):
        # ToDo: Implement this method.
        pass

    def more_results(self):
        # ToDo: Implement this method.
        pass

    def intersects(self):
        # ToDo: Implement this method.
        pass

    def nested_search(self):
        # ToDo: Implement this method.
        pass

    def search_for_document(self):
        # ToDo: Implement this method.
        pass

    def fast_search_for_document(self):
        # ToDo: Implement this method.
        pass

    # Answers Methods

    def ask(self):
        # ToDo: Implement this method.
        pass

    def generate_search_from_question(self):
        # ToDo: Implement this method.
        pass

    def is_question(self):
        # ToDo: Implement this method.
        pass

    # A.I. Methods

    def list_inferences(self):
        # ToDo: Implement this method.
        pass

    # Resume Methods

    def summarize_document(self):
        # ToDo: Implement this method.
        pass

    def summarize_subject(self):
        # ToDo: Implement this method.
        pass

    # Tags Extraction Methods

    def extract_tags(self):
        # ToDo: Implement this method.
        pass

    def tag_cloud(self):
        # ToDo: Implement this method.
        pass

    def extract_tag_connected_entities(self):
        # ToDo: Implement this method.
        pass

    # Document Comparison Methods

    def compare_docs_version(self):
        # ToDo: Implement this method.
        pass

    # Generate Questions Methods

    def questionize_document(self):
        # ToDo: Implement this method.
        pass

    def questionize_subject(self):
        # ToDo: Implement this method.
        pass

    def outline(self):
        # ToDo: Implement this method.
        pass

    def metrics(self):
        # ToDo: Implement this method.
        pass

    # User Management Methods

    def check_user(self):
        # ToDo: Implement this method.
        pass

    def create_user(self):
        # ToDo: Implement this method.
        pass

    def list_users(self):
        # ToDo: Implement this method.
        pass

    def change_password(self):
        # ToDo: Implement this method.
        pass

    def delete_user(self):
        # ToDo: Implement this method.
        pass

    # Reports and Statistics Methods

    def no_answers(self):
        # ToDo: Implement this method.
        pass

    def stats(self):
        # ToDo: Implement this method.
        pass

    def queries_for_word(self):
        # ToDo: Implement this method.
        pass

    def queries_for_token(self):
        # ToDo: Implement this method.
        pass

    def flush_stats(self):
        # ToDo: Implement this method.
        pass

    def increment_rank_score(self):
        # ToDo: Implement this method.
        pass


