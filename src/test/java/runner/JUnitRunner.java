package runner;

import org.junit.runner.RunWith;

import io.cucumber.junit.Cucumber;
import io.cucumber.junit.CucumberOptions;

@RunWith(Cucumber.class)
@CucumberOptions(features="./src/test/resources/features/Login.feature",
glue={"com.example.stepdefinitions"},
//plugin = { "pretty",
//"html:target/cucumber-reports.html" })
plugin = { "pretty",
"com.aventstack.extentreports.cucumber.adapter.ExtentCucumberAdapter:" }
)
public class JUnitRunner {

}
