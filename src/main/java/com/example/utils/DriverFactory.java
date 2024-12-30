package com.example.utils;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class DriverFactory {
	public static WebDriver driver=null;
	
	public static WebDriver getDriver()
	{
		if(driver==null)
		{
//			System.setProperty("webdriver.chrome.driver", "./src/main/resources/drivers/chromedriver.exe");
			driver = new ChromeDriver();
//			driver.manage().window().maximize();
		}
		return driver;
	}
	
	public static void quitDriver()
	{
		if(driver!=null)
		{
			driver.quit();
			driver=null;
		}
	}
}
