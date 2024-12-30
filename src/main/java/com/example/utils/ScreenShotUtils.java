package com.example.utils;

import java.io.File;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Date;

import org.apache.commons.io.FileUtils;
import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;
import org.openqa.selenium.WebDriver;

public class ScreenShotUtils {
	public static void captureScreenshot(WebDriver driver, String screenshotName) {
        // Take screenshot and store it as a file
        File scrFile = ((TakesScreenshot) driver).getScreenshotAs(OutputType.FILE);
        
        // Create the directory path to store the screenshot (e.g., "target/screenshots")
        String directoryPath = "target/screenshots/";
        new File(directoryPath).mkdirs();  // Create directory if it doesn't exist
        
        // Generate a timestamped filename
        String timestamp = new SimpleDateFormat("yyyyMMdd_HHmmss").format(new Date());
        String fileName = directoryPath + screenshotName + "_" + timestamp + ".png";
        
        // Copy the screenshot to the desired location
        try {
            FileUtils.copyFile(scrFile, new File(fileName));
            System.out.println("Screenshot saved to " + fileName);
        } catch (IOException e) {
            System.err.println("Error saving screenshot: " + e.getMessage());
        }
    }

}
