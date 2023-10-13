Here is how you create HTML Webpages using PowerShell.

First Open PowerShell ISE and enter the following command:

Install-Module -Name PSHTML -Scope CurrentUser -Force
Or  (if you have Administrative permissions)
Install_Module PSHTML

If

This will install the module into the current user’s directory. This helps avoid the need for administrative privileges/rights

Verify that it’s installed by typing

 Get-Command  -Module PSHTML

You will see a list of Commands that are associated with the module. Here are some example webpage commands:


Example 1:
 In the script pane of PowerShell ISE enter the following command:


html{ 
head {title 'Hell0 world’}

h1 {'Welcome to my webpage'
}
body{
p ‘This is my first webpage'
}
} | Set-Content -Path Hello. html
Invoke-Item -Path Hello. html

Click the green play button or f5 to run the program 

The code above will display a webpage with “Welcome to my webpage” as the page header and “This is my first webpage” in the body of the page. The command Set-Content -Path Hello.html will create a HTML file with the code you created. Then Invoke-Item -Path Hello. html will open the file in your preferred webpage. 

Example 2:

html{ 
    head{title 'Hell0 World ' 
   } 
   h1{'Welcome to my webpage'} 

   body{ 

   p 'This is my first webpage' 

   p 'My Favorite fruit is:' 

   li { 'Apple' 
} 

   li { 'Pear' 
 }   

li { 'Banana'
   } 
} 

} | Set-Content -Path Hello.html 
Invoke-Item -Path Hello.html 

This example uses the li  function to create a bulleted list in HTML.

Example 3:

html{  head{title 'Hell0 World ' 
	} 

   h1{'Welcome to my webpage'
	} 

   body{ 
   p 'This is my first webpage' 

   p 'Styles:' 
   li { b 'This is a bold statement' 
	} 

   li { i 'Take that italicized' 
  	 }   
   } 
} | Set-Content -Path Hello.html 
Invoke-Item -Path Hello.html 

Finally, adding “i” in front of text will italicize it, and putting “b” in front of the text will bold it.
