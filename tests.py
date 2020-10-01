from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app


client = TestClient(app)

#ROOT
def test_read_root():
    response = client.get("/")
    assert response.status_code == 200

# CONTACTS TESTING
def test_read_contacts():
    response = client.get("/contacts/")
    assert response.status_code == 200

def test_read_contact_return_200():
    response = client.get("/contact/1")
    assert response.status_code == 200

def test_read_contact_return_404_with_correct_id_type():
    response = client.get("/contact/30000")
    assert response.status_code == 404
    assert response.json() == {"detail":"contact not found"}

def test_read_contact_return_404_wrong_id_type():
    response = client.get("/contact/8JKL")
    assert response.status_code == 404
    assert response.json() == {"detail":"invalid contact id. contact id must be an integer  "}

# COMPANIES TESTING
def test_read_companies():
    response = client.get("/companies/")
    assert response.status_code == 200

def test_read_company_return_200():
    response = client.get("/company/1")
    assert response.status_code == 200

def test_read_company_return_404_with_correct_id_type():
    response = client.get("/company/30000")
    assert response.status_code == 404
    assert response.json() == {"detail":"company not found"}

def test_read_company_return_404_wrong_id_type():
    response = client.get("/company/sfjk")
    assert response.status_code == 404
    assert response.json() == {"detail":"invalid company id. contact id must be an integer  "}

# ACTIVITY AREAS TESTING
def test_read_activityareas():
    response = client.get("/activityareas/")
    assert response.status_code == 200

def test_read_activityarea_return_200():
    response = client.get("/activityarea/1")
    assert response.status_code == 200

def test_read_activityarea_return_404_with_correct_id_type():
    response = client.get("/activityarea/30000")
    assert response.status_code == 404
    assert response.json() == {"detail":"activity area not found"}

def test_read_activityarea_return_404_wrong_id_type():
    response = client.get("/activityarea/sfjk")
    assert response.status_code == 404
    assert response.json() == {"detail":"invalid activity area id. contact id must be an integer  "}


# SEARCH TESTING
def test_search_return_contact_with_200():
    response = client.get('/search/?query=Alicia')
    assert response.status_code == 200

def test_search_return_company_with_200():
    response = client.get('/search/?query=Technology')
    assert response.status_code == 200

def test_search_return_activityarea_with_200():
    response = client.get('/search/?query=IPNET')
    assert response.status_code == 200

def test_search_return_404():
    response = client.get('/search/?query=smdfkdj8484JDK')
    assert response.status_code == 404
    assert response.json() == {"detail":"item not found"}