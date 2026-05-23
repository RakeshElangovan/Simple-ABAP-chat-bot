from app.core.intent_engine import IntentEngine


def test_intent_detection():

    engine = IntentEngine()

    intent = engine.detect_intent("hello")

    assert intent == "greeting"
