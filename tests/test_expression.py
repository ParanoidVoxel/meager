import meager.router as router

router = router.Router()

def test_router_no_val():
    exp = router.create_route_expression("/test")
    assert exp.match("/test")
    assert not(exp.match("/asd"))
    assert not(exp.match("/test/"))

def test_router_one_val():
    exp = router.create_route_expression("/test/<value_1>")
    assert exp.match("/test/1")
    assert exp.match("/test/str")
    assert not(exp.match("/asd"))
    assert not(exp.match("/test"))
    assert not(exp.match(""))

def test_router_two_val():
    exp = router.create_route_expression("/test/<value_1>/<value_2>")
    assert exp.match("/test/1/str")
    assert exp.match("/test/str/1")
    assert not(exp.match("/asd"))
    assert not(exp.match("/test/asd"))
    assert not(exp.match(""))


