package com.example.pages;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

import junit.framework.Assert;

public class LoginPage extends BaseClass
{
//	WebDriver driver=null;
	
	@FindBy(xpath="//input[@id=\"user-name\"]")
	WebElement usernameField;
	
	@FindBy(xpath="//input[@placeholder=\"Password\"]")
	WebElement passwordField;
	
	@FindBy(xpath="//input[@id=\"login-button\"]")
	WebElement loginButton;
	
	@FindBy(xpath="//*[@id=\"login_button_container\"]/div/form/div[3]/h3")
	WebElement errorMsg;
	
	public LoginPage(WebDriver driver)
	{
//		this.driver=driver;
//		PageFactory.initElements(driver, this);
		super(driver);
	}
	
	public void enterUsername(String username)
	{
		usernameField.sendKeys(username);
	}
	
	public void enterPassword(String password)
	{
		passwordField.sendKeys(password);
	}
	
	public void loginButtonClick() {
		loginButton.click();
	}
	
	public void verifyErrorMsg(String errorMsg1)
	{
		Assert.assertEquals(errorMsg.getText(),errorMsg1);
	}
}
