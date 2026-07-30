from app.graph.agent import agent


def test_agent_runs():
    result = agent.invoke(
        {
            "message": "List all tables",
            "messages": [],
        }
    )

    assert "response" in result
    assert result["response"] is not None