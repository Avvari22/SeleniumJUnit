package com.example.stepdefinitions;

import static org.junit.Assert.assertEquals;

import org.openqa.selenium.WebDriver;

import com.example.pages.LoginPage;
import com.example.utils.DriverFactory;
import com.example.utils.ScreenShotUtils;

import io.cucumber.java.After;
import io.cucumber.java.Before;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;

public class LoginSteps {
	WebDriver driver = null;
	LoginPage loginPage = null;

	@Before
	public void beforeSteps() {
		driver = DriverFactory.getDriver();
		loginPage = new LoginPage(driver);
	}
	
	@After
	public void afterSteps() {
		DriverFactory.quitDriver();
	}

	@Given("Navigation should happen {string}")
	public void navigation_should_happen(String url) {
		// Write code here that turns the phrase above into concrete actions
		// throw new io.cucumber.java.PendingException();
		driver.get(url);
	}

	@When("User enter {string} username")
	public void user_enter_username(String name) {
		// Write code here that turns the phrase above into concrete actions
//	    throw new io.cucumber.java.PendingException();
//		username = driver.findElement(By.xpath("//input[@id=\"user-name\"]"));
//		username.sendKeys(name);
		loginPage.enterUsername(name);
	}

	@When("User enter {string} password")
	public void user_enter_password(String password1) {
		// Write code here that turns the phrase above into concrete actions
//	    throw new io.cucumber.java.PendingException();
//		password = driver.findElement(By.xpath("//input[@placeholder=\"Password\"]"));
//		password.sendKeys(password1);
		loginPage.enterPassword(password1);
	}

	@When("User click Login button")
	public void user_click_login_button() {
		// Write code here that turns the phrase above into concrete actions
//		submit = driver.findElement(By.xpath("//input[@id=\"login-button\"]"));
//		submit.click();
//	    throw new io.cucumber.java.PendingException();
		loginPage.loginButtonClick();
	}

	@Then("Verify user login successfully with {string}")
	public void verify_user_login_successfully_with(String errorMsg) {
		// Write code here that turns the phrase above into concrete actions
//	    throw new io.cucumber.java.PendingException();
		String url = driver.getCurrentUrl().toString();
		if(url.contains("inventory.html"))
		{
			assertEquals(url, "https://www.saucedemo.com/inventory.html");
		}
		else
		{
			loginPage.verifyErrorMsg(errorMsg);
			ScreenShotUtils.captureScreenshot(driver, "InvalidLoginError");
		}
	}
	
//	@Then("Verify Error message for invalid credentials")
//	public void verify_error_message_for_invalid_credentials() {
//	    // Write code here that turns the phrase above into concrete actions
////	    throw new io.cucumber.java.PendingException();
////		WebElement errorMsg=driver.findElement(By.xpath("//*[@id=\"login_button_container\"]/div/form/div[3]/h3"));
////		System.out.println("String is:"+errorMsg.getText());
//		
////		loginPage.verifyErrorMsg();
//		ScreenShotUtils.captureScreenshot(driver, "InvalidLoginError");
//	}
	

}
