package runner;

import io.cucumber.testng.CucumberOptions;

@CucumberOptions(features="./src/test/resources/features/Login.feature",
glue={"stepdefinitions"},
plugin = { "pretty",
"html:target/cucumber-reports.html" })
public class TestNGRunner 
{

}