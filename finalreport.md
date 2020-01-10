report #20200109-9629

# WP Guardian Vulnerability Scan

### 09/01/2020 20:01:23

## Domain

http://3.82.102.163/wordpress

## Summary 


 > 

## Vulnerabilities  

### *Wordpress Version: 4.6.1*


 --- 
 ### **CVE-2017-5611**

**CVSS Score:** 

 7.5

**CVSS Vector:** 

 AV:N/AC:L/Au:N/C:P/I:P/A:P

>SQL injection vulnerability in wp-includes/class-wp-query.php in WP_Query in WordPress before 4.7.2 allows remote attackers to execute arbitrary SQL commands by leveraging the presence of an affected plugin or theme that mishandles a crafted post type name.

References:

>https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2017-5611

 --- 
 ### **CVE-2017-14723**

**CVSS Score:** 

 7.5

**CVSS Vector:** 

 AV:N/AC:L/Au:N/C:P/I:P/A:P

>Before version 4.8.2, WordPress mishandled % characters and additional placeholder values in $wpdb->prepare, and thus did not properly address the possibility of plugins and themes enabling SQL injection attacks.

References:

>https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2017-14723

 --- 
 ### **CVE-2017-16510**

**CVSS Score:** 

 7.5

**CVSS Vector:** 

 AV:N/AC:L/Au:N/C:P/I:P/A:P

>WordPress before 4.8.3 is affected by an issue where $wpdb->prepare() can create unexpected and unsafe queries leading to potential SQL injection (SQLi) in plugins and themes, as demonstrated by a "double prepare" approach, a different vulnerability than CVE-2017-14723.

References:

>https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2017-16510

 --- 
 ### **CVE-2018-20148**

**CVSS Score:** 

 7.5

**CVSS Vector:** 

 AV:N/AC:L/Au:N/C:P/I:P/A:P

>In WordPress before 4.9.9 and 5.x before 5.0.1, contributors could conduct PHP object injection attacks via crafted metadata in a wp.getMediaItem XMLRPC call. This is caused by mishandling of serialized data at phar:// URLs in the wp_get_attachment_thumb_file function in wp-includes/post.php.

References:

>https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2018-20148

 --- 
 ### **CVE-2019-17669**

**CVSS Score:** 

 7.5

**CVSS Vector:** 

 AV:N/AC:L/Au:N/C:P/I:P/A:P

>WordPress before 5.2.4 has a Server Side Request Forgery (SSRF) vulnerability because URL validation does not consider the interpretation of a name as a series of hex characters.

References:

>https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2019-17669

 --- 
 ### **CVE-2019-17670**

**CVSS Score:** 

 7.5

**CVSS Vector:** 

 AV:N/AC:L/Au:N/C:P/I:P/A:P

>WordPress before 5.2.4 has a Server Side Request Forgery (SSRF) vulnerability because Windows paths are mishandled during certain validation of relative URLs.

References:

>https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2019-17670

 --- 
 ### **CVE-2019-20041**

**CVSS Score:** 

 7.5

**CVSS Vector:** 

 AV:N/AC:L/Au:N/C:P/I:P/A:P

>wp_kses_bad_protocol in wp-includes/kses.php in WordPress before 5.3.1 mishandles the HTML5 colon named entity, allowing attackers to bypass input sanitization, as demonstrated by the javascript&colon; substring.

References:

>https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2019-20041

 --- 
 ### **CVE-2017-5492**

**CVSS Score:** 

 6.8

**CVSS Vector:** 

 AV:N/AC:M/Au:N/C:P/I:P/A:P

>Cross-site request forgery (CSRF) vulnerability in the widget-editing accessibility-mode feature in WordPress before 4.7.1 allows remote attackers to hijack the authentication of unspecified victims for requests that perform a widgets-access action, related to wp-admin/includes/class-wp-screen.php and wp-admin/widgets.php.

References:

>https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2017-5492

 --- 
 ### **CVE-2017-9064**

**CVSS Score:** 

 6.8

**CVSS Vector:** 

 AV:N/AC:M/Au:N/C:P/I:P/A:P

>In WordPress before 4.7.5, a Cross Site Request Forgery (CSRF) vulnerability exists in the filesystem credentials dialog because a nonce is not required for updating credentials.

References:

>https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2017-9064

 --- 
 ### **CVE-2019-9787**

**CVSS Score:** 

 6.8

**CVSS Vector:** 

 AV:N/AC:M/Au:N/C:P/I:P/A:P

>WordPress before 5.1.1 does not properly filter comment content, leading to Remote Code Execution by unauthenticated users in a default configuration. This occurs because CSRF protection is mishandled, and because Search Engine Optimization of A elements is performed incorrectly, leading to XSS. The XSS results in administrative access, which allows arbitrary changes to .php files. This is related to wp-admin/includes/ajax-actions.php and wp-includes/comment.php.

References:

>https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2019-9787

 --- 
 ### **CVE-2019-17675**

**CVSS Score:** 

 6.8

**CVSS Vector:** 

 AV:N/AC:M/Au:N/C:P/I:P/A:P

>WordPress before 5.2.4 does not properly consider type confusion during validation of the referer in the admin pages, possibly leading to CSRF.

References:

>https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2019-17675

 --- 
 ### **CVE-2017-17091**

**CVSS Score:** 

 6.5

**CVSS Vector:** 

 AV:N/AC:L/Au:S/C:P/I:P/A:P

>wp-admin/user-new.php in WordPress before 4.9.1 sets the newbloguser key to a string that can be directly derived from the user ID, which allows remote attackers to bypass intended access restrictions by entering this string.

References:

>https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2017-17091

 --- 
 ### **CVE-2018-12895**

**CVSS Score:** 

 6.5

**CVSS Vector:** 

 AV:N/AC:L/Au:S/C:P/I:P/A:P

>WordPress through 4.9.6 allows Author users to execute arbitrary code by leveraging directory traversal in the wp-admin/post.php thumb parameter, which is passed to the PHP unlink function and can delete the wp-config.php file. This is related to missing filename validation in the wp-includes/post.php wp_delete_attachment function. The attacker must have capabilities for files and posts that are normally available only to the Author, Editor, and Administrator roles. The attack methodology is to delete wp-config.php and then launch a new installation process to increase the attacker's privileges.

References:

>https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2018-12895

 --- 
 ### **CVE-2019-8942**

**CVSS Score:** 

 6.5

**CVSS Vector:** 

 AV:N/AC:L/Au:S/C:P/I:P/A:P

>WordPress before 4.9.9 and 5.x before 5.0.1 allows remote code execution because an _wp_attached_file Post Meta entry can be changed to an arbitrary string, such as one ending with a .jpg?file.php substring. An attacker with author privileges can execute arbitrary code by uploading a crafted image containing PHP code in the Exif metadata. Exploitation can leverage CVE-2019-8943.

References:

>https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2019-8942

 --- 
 ### **CVE-2017-6815**

**CVSS Score:** 

 5.8

**CVSS Vector:** 

 AV:N/AC:M/Au:N/C:P/I:P/A:N

>In WordPress before 4.7.3 (wp-includes/pluggable.php), control characters can trick redirect URL validation.

References:

>https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2017-6815

 --- 
 ### **CVE-2018-10101**

**CVSS Score:** 

 5.8

**CVSS Vector:** 

 AV:N/AC:M/Au:N/C:P/I:P/A:N

>Before WordPress 4.9.5, the URL validator assumed URLs with the hostname localhost were on the same host as the WordPress server.

References:

>https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2018-10101

 --- 
 ### **CVE-2018-10100**

**CVSS Score:** 

 5.8

**CVSS Vector:** 

 AV:N/AC:M/Au:N/C:P/I:P/A:N

>Before WordPress 4.9.5, the redirection URL for the login page was not validated or sanitized if forced to use HTTPS.

References:

>https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2018-10100

 --- 
 ### **CVE-2018-20147**

**CVSS Score:** 

 5.5

**CVSS Vector:** 

 AV:N/AC:L/Au:S/C:N/I:P/A:P

>In WordPress before 4.9.9 and 5.x before 5.0.1, authors could modify metadata to bypass intended restrictions on deleting files.

References:

>https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2018-20147

 --- 
 ### **CVE-2017-5491**

**CVSS Score:** 

 5.0

**CVSS Vector:** 

 AV:N/AC:L/Au:N/C:N/I:P/A:N

>wp-mail.php in WordPress before 4.7.1 might allow remote attackers to bypass intended posting restrictions via a spoofed mail server with the mail.example.com name.

References:

>https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2017-5491

 --- 
 ### **CVE-2017-5493**

**CVSS Score:** 

 5.0

**CVSS Vector:** 

 AV:N/AC:L/Au:N/C:N/I:P/A:N

>wp-includes/ms-functions.php in the Multisite WordPress API in WordPress before 4.7.1 does not properly choose random numbers for keys, which makes it easier for remote attackers to bypass intended access restrictions via a crafted (1) site signup or (2) user signup.

References:

>https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2017-5493

 --- 
 ### **CVE-2017-5610**

**CVSS Score:** 

 5.0

**CVSS Vector:** 

 AV:N/AC:L/Au:N/C:P/I:N/A:N

>wp-admin/includes/class-wp-press-this.php in Press This in WordPress before 4.7.2 does not properly restrict visibility of a taxonomy-assignment user interface, which allows remote attackers to bypass intended access restrictions by reading terms.

References:

>https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2017-5610

 --- 
 ### **CVE-2017-9066**

**CVSS Score:** 

 5.0

**CVSS Vector:** 

 AV:N/AC:L/Au:N/C:N/I:P/A:N

>In WordPress before 4.7.5, there is insufficient redirect validation in the HTTP class, leading to SSRF.

References:

>https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2017-9066

 --- 
 ### **CVE-2017-9062**

**CVSS Score:** 

 5.0

**CVSS Vector:** 

 AV:N/AC:L/Au:N/C:N/I:P/A:N

>In WordPress before 4.7.5, there is improper handling of post meta data values in the XML-RPC API.

References:

>https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2017-9062

 --- 
 ### **CVE-2017-9065**

**CVSS Score:** 

 5.0

**CVSS Vector:** 

 AV:N/AC:L/Au:N/C:N/I:P/A:N

>In WordPress before 4.7.5, there is a lack of capability checks for post meta data in the XML-RPC API.

References:

>https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2017-9065

 --- 
 ### **CVE-2017-14719**

**CVSS Score:** 

 5.0

**CVSS Vector:** 

 AV:N/AC:L/Au:N/C:P/I:N/A:N

>Before version 4.8.2, WordPress was vulnerable to a directory traversal attack during unzip operations in the ZipArchive and PclZip components.

References:

>https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2017-14719

 --- 
 ### **CVE-2018-6389**

**CVSS Score:** 

 5.0

**CVSS Vector:** 

 AV:N/AC:L/Au:N/C:N/I:N/A:P

>In WordPress through 4.9.2, unauthenticated attackers can cause a denial of service (resource consumption) by using the large list of registered .js files (from wp-includes/script-loader.php) to construct a series of requests to load every file many times.

References:

>https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2018-6389

 --- 
 ### **CVE-2018-20151**

**CVSS Score:** 

 5.0

**CVSS Vector:** 

 AV:N/AC:L/Au:N/C:P/I:N/A:N

>In WordPress before 4.9.9 and 5.x before 5.0.1, the user-activation page could be read by a search engine's web crawler if an unusual configuration were chosen. The search engine could then index and display a user's e-mail address and (rarely) the password that was generated by default.

References:

>https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2018-20151

 --- 
 ### **CVE-2019-17671**

**CVSS Score:** 

 5.0

**CVSS Vector:** 

 AV:N/AC:L/Au:N/C:P/I:N/A:N

>In WordPress before 5.2.4, unauthenticated viewing of certain content is possible because the static query property is mishandled.

References:

>https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2019-17671

 --- 
 ### **CVE-2019-17673**

**CVSS Score:** 

 5.0

**CVSS Vector:** 

 AV:N/AC:L/Au:N/C:N/I:P/A:N

>WordPress before 5.2.4 is vulnerable to poisoning of the cache of JSON GET requests because certain requests lack a Vary: Origin header.

References:

>https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2019-17673

 --- 
 ### **CVE-2019-20043**

**CVSS Score:** 

 5.0

**CVSS Vector:** 

 AV:N/AC:L/Au:N/C:N/I:P/A:N

>WordPress before 5.3.1 allowed an unauthenticated user to make a post sticky through the REST API because of missing access control in wp-includes/rest-api/endpoints/class-wp-rest-posts-controller.php.

References:

>https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2019-20043

 --- 
 ### **CVE-2017-14725**

**CVSS Score:** 

 4.9

**CVSS Vector:** 

 AV:N/AC:M/Au:S/C:P/I:P/A:N

>Before version 4.8.2, WordPress was susceptible to an open redirect attack in wp-admin/edit-tag-form.php and wp-admin/user-edit.php.

References:

>https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2017-14725

 --- 
 ### **CVE-2017-5488**

**CVSS Score:** 

 4.3

**CVSS Vector:** 

 AV:N/AC:M/Au:N/C:N/I:P/A:N

>Multiple cross-site scripting (XSS) vulnerabilities in wp-admin/update-core.php in WordPress before 4.7.1 allow remote attackers to inject arbitrary web script or HTML via the (1) name or (2) version header of a plugin.

References:

>https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2017-5488

 --- 
 ### **CVE-2017-5490**

**CVSS Score:** 

 4.3

**CVSS Vector:** 

 AV:N/AC:M/Au:N/C:N/I:P/A:N

>Cross-site scripting (XSS) vulnerability in the theme-name fallback functionality in wp-includes/class-wp-theme.php in WordPress before 4.7.1 allows remote attackers to inject arbitrary web script or HTML via a crafted directory name of a theme, related to wp-admin/includes/class-theme-installer-skin.php.

References:

>https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2017-5490

 --- 
 ### **CVE-2017-5612**

**CVSS Score:** 

 4.3

**CVSS Vector:** 

 AV:N/AC:M/Au:N/C:N/I:P/A:N

>Cross-site scripting (XSS) vulnerability in wp-admin/includes/class-wp-posts-list-table.php in the posts list table in WordPress before 4.7.2 allows remote attackers to inject arbitrary web script or HTML via a crafted excerpt.

References:

>https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2017-5612

 --- 
 ### **CVE-2017-6819**

**CVSS Score:** 

 4.3

**CVSS Vector:** 

 AV:N/AC:M/Au:N/C:N/I:N/A:P

>In WordPress before 4.7.3, there is cross-site request forgery (CSRF) in Press This (wp-admin/includes/class-wp-press-this.php), leading to excessive use of server resources. The CSRF can trigger an outbound HTTP request for a large file that is then parsed by Press This.

References:

>https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2017-6819

 --- 
 ### **CVE-2017-8295**

**CVSS Score:** 

 4.3

**CVSS Vector:** 

 AV:N/AC:M/Au:N/C:N/I:P/A:N

>WordPress through 4.7.4 relies on the Host HTTP header for a password-reset e-mail message, which makes it easier for remote attackers to reset arbitrary passwords by making a crafted wp-login.php?action=lostpassword request and then arranging for this message to bounce or be resent, leading to transmission of the reset key to a mailbox on an attacker-controlled SMTP server. This is related to problematic use of the SERVER_NAME variable in wp-includes/pluggable.php in conjunction with the PHP mail function. Exploitation is not achievable in all cases because it requires at least one of the following: (1) the attacker can prevent the victim from receiving any e-mail messages for an extended period of time (such as 5 days), (2) the victim's e-mail system sends an autoresponse containing the original message, or (3) the victim manually composes a reply containing the original message.

References:

>https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2017-8295

 --- 
 ### **CVE-2017-9061**

**CVSS Score:** 

 4.3

**CVSS Vector:** 

 AV:N/AC:M/Au:N/C:N/I:P/A:N

>In WordPress before 4.7.5, a cross-site scripting (XSS) vulnerability exists when attempting to upload very large files, because the error message does not properly restrict presentation of the filename.

References:

>https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2017-9061

 --- 
 ### **CVE-2017-9063**

**CVSS Score:** 

 4.3

**CVSS Vector:** 

 AV:N/AC:M/Au:N/C:N/I:P/A:N

>In WordPress before 4.7.5, a cross-site scripting (XSS) vulnerability related to the Customizer exists, involving an invalid customization session.

References:

>https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2017-9063

 --- 
 ### **CVE-2017-14724**

**CVSS Score:** 

 4.3

**CVSS Vector:** 

 AV:N/AC:M/Au:N/C:N/I:P/A:N

>Before version 4.8.2, WordPress was vulnerable to cross-site scripting in oEmbed discovery.

References:

>https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2017-14724

 --- 
 ### **CVE-2017-14726**

**CVSS Score:** 

 4.3

**CVSS Vector:** 

 AV:N/AC:M/Au:N/C:N/I:P/A:N

>Before version 4.8.2, WordPress was vulnerable to a cross-site scripting attack via shortcodes in the TinyMCE visual editor.

References:

>https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2017-14726

 --- 
 ### **CVE-2018-5776**

**CVSS Score:** 

 4.3

**CVSS Vector:** 

 AV:N/AC:M/Au:N/C:N/I:P/A:N

>WordPress before 4.9.2 has XSS in the Flash fallback files in MediaElement (under wp-includes/js/mediaelement).

References:

>https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2018-5776

 --- 
 ### **CVE-2018-10102**

**CVSS Score:** 

 4.3

**CVSS Vector:** 

 AV:N/AC:M/Au:N/C:N/I:P/A:N

>Before WordPress 4.9.5, the version string was not escaped in the get_the_generator function, and could lead to XSS in a generator tag.

References:

>https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2018-10102

 --- 
 ### **CVE-2018-20150**

**CVSS Score:** 

 4.3

**CVSS Vector:** 

 AV:N/AC:M/Au:N/C:N/I:P/A:N

>In WordPress before 4.9.9 and 5.x before 5.0.1, crafted URLs could trigger XSS for certain use cases involving plugins.

References:

>https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2018-20150

 --- 
 ### **CVE-2019-16222**

**CVSS Score:** 

 4.3

**CVSS Vector:** 

 AV:N/AC:M/Au:N/C:N/I:P/A:N

>WordPress before 5.2.3 has an issue with URL sanitization in wp_kses_bad_protocol_once in wp-includes/kses.php that can lead to cross-site scripting (XSS) attacks.

References:

>https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2019-16222

 --- 
 ### **CVE-2019-17672**

**CVSS Score:** 

 4.3

**CVSS Vector:** 

 AV:N/AC:M/Au:N/C:N/I:P/A:N

>WordPress before 5.2.4 is vulnerable to a stored XSS attack to inject JavaScript into STYLE elements.

References:

>https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2019-17672

 --- 
 ### **CVE-2019-20042**

**CVSS Score:** 

 4.3

**CVSS Vector:** 

 AV:N/AC:M/Au:N/C:N/I:P/A:N

>WordPress before 5.3.1 allowed an attacker to create a cross-site scripting attack (XSS) in well crafted links, because of an insufficient protection mechanism in wp_targeted_link_rel in wp-includes/formatting.php.

References:

>https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2019-20042

 --- 
 ### **CVE-2018-20152**

**CVSS Score:** 

 4.0

**CVSS Vector:** 

 AV:N/AC:L/Au:S/C:N/I:P/A:N

>In WordPress before 4.9.9 and 5.x before 5.0.1, authors could bypass intended restrictions on post types via crafted input.

References:

>https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2018-20152

 --- 
 ### **CVE-2019-8943**

**CVSS Score:** 

 4.0

**CVSS Vector:** 

 AV:N/AC:L/Au:S/C:N/I:P/A:N

>WordPress through 5.0.3 allows Path Traversal in wp_crop_image(). An attacker (who has privileges to crop an image) can write the output image to an arbitrary directory via a filename containing two image extensions and ../ sequences, such as a filename ending with the .jpg?/../../file.jpg substring.

References:

>https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2019-8943

 --- 
 ### **CVE-2017-6814**

**CVSS Score:** 

 3.5

**CVSS Vector:** 

 AV:N/AC:M/Au:S/C:N/I:P/A:N

>In WordPress before 4.7.3, there is authenticated Cross-Site Scripting (XSS) via Media File Metadata. This is demonstrated by both (1) mishandling of the playlist shortcode in the wp_playlist_shortcode function in wp-includes/media.php and (2) mishandling of meta information in the renderTracks function in wp-includes/js/mediaelement/wp-playlist.js.

References:

>https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2017-6814

 --- 
 ### **CVE-2017-6817**

**CVSS Score:** 

 3.5

**CVSS Vector:** 

 AV:N/AC:M/Au:S/C:N/I:P/A:N

>In WordPress before 4.7.3 (wp-includes/embed.php), there is authenticated Cross-Site Scripting (XSS) in YouTube URL Embeds.

References:

>https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2017-6817

 --- 
 ### **CVE-2017-17092**

**CVSS Score:** 

 3.5

**CVSS Vector:** 

 AV:N/AC:M/Au:S/C:N/I:P/A:N

>wp-includes/functions.php in WordPress before 4.9.1 does not require the unfiltered_html capability for upload of .js files, which might allow remote attackers to conduct XSS attacks via a crafted file.

References:

>https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2017-17092

 --- 
 ### **CVE-2017-17094**

**CVSS Score:** 

 3.5

**CVSS Vector:** 

 AV:N/AC:M/Au:S/C:N/I:P/A:N

>wp-includes/feed.php in WordPress before 4.9.1 does not properly restrict enclosures in RSS and Atom fields, which might allow attackers to conduct XSS attacks via a crafted URL.

References:

>https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2017-17094

 --- 
 ### **CVE-2017-17093**

**CVSS Score:** 

 3.5

**CVSS Vector:** 

 AV:N/AC:M/Au:S/C:N/I:P/A:N

>wp-includes/general-template.php in WordPress before 4.9.1 does not properly restrict the lang attribute of an HTML element, which might allow attackers to conduct XSS attacks via the language setting of a site.

References:

>https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2017-17093

 --- 
 ### **CVE-2018-20153**

**CVSS Score:** 

 3.5

**CVSS Vector:** 

 AV:N/AC:M/Au:S/C:N/I:P/A:N

>In WordPress before 4.9.9 and 5.x before 5.0.1, contributors could modify new comments made by users with greater privileges, possibly causing XSS.

References:

>https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2018-20153

 --- 
 ### **CVE-2018-20149**

**CVSS Score:** 

 3.5

**CVSS Vector:** 

 AV:N/AC:M/Au:S/C:N/I:P/A:N

>In WordPress before 4.9.9 and 5.x before 5.0.1, when the Apache HTTP Server is used, authors could upload crafted files that bypass intended MIME type restrictions, leading to XSS, as demonstrated by a .jpg file without JPEG data.

References:

>https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2018-20149

 --- 
 ### **CVE-2019-17674**

**CVSS Score:** 

 3.5

**CVSS Vector:** 

 AV:N/AC:M/Au:S/C:N/I:P/A:N

>WordPress before 5.2.4 is vulnerable to stored XSS (cross-site scripting) via the Customizer.

References:

>https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2019-17674

 --- 
 ### **CVE-2019-16781**

**CVSS Score:** 

 3.5

**CVSS Vector:** 

 AV:N/AC:M/Au:S/C:N/I:P/A:N

>In WordPress before 5.3.1, authenticated users with lower privileges (like contributors) can inject JavaScript code in the block editor, which is executed within the dashboard. It can lead to an admin opening the affected post in the editor leading to XSS.

References:

>https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2019-16781

 --- 
 ### **CVE-2019-16780**

**CVSS Score:** 

 3.5

**CVSS Vector:** 

 AV:N/AC:M/Au:S/C:N/I:P/A:N

>WordPress users with lower privileges (like contributors) can inject JavaScript code in the block editor using a specific payload, which is executed within the dashboard. This can lead to XSS if an admin opens the post in the editor. Execution of this attack does require an authenticated user. This has been patched in WordPress 5.3.1, along with all the previous WordPress versions from 3.7 to 5.3 via a minor release. Automatic updates are enabled by default for minor releases and we strongly recommend that you keep them enabled.

References:

>https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2019-16780

 --- 
 ### **CVE-2016-9263**

**CVSS Score:** 

 2.6

**CVSS Vector:** 

 AV:N/AC:H/Au:N/C:N/I:P/A:N

>WordPress through 4.8.2, when domain-based flashmediaelement.swf sandboxing is not used, allows remote attackers to conduct cross-domain Flash injection (XSF) attacks by leveraging code contained within the wp-includes/js/mediaelement/flashmediaelement.swf file.

References:

>https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2016-9263

 --- 
 ### **CVE-2019-16788**

**CVSS Score:** 

 0.0

**CVSS Vector:** 

 NONE

>In WordPress versions from 3.7 to 5.3.0, authenticated users who do not have the rights to publish a post are able to mark posts as sticky or unsticky via the REST API. For example, the contributor role does not have such rights, but this allowed them to bypass that. This has been patched in WordPress 5.3.1, along with all the previous WordPress versions from 3.7 to 5.3 via a minor release. Automatic updates are enabled by default for minor releases and we strongly recommend that you keep them enabled.

References:

>https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2019-16788

 --- 
 ### **CVE-2019-16773**

**CVSS Score:** 

 0.0

**CVSS Vector:** 

 NONE

>In WordPress versions from 3.7 to 5.3.0, the function wp_targeted_link_rel() can be used in a particular way to result in a stored cross-site scripting (XSS) vulnerability. This has been patched in WordPress 5.3.1, along with all the previous WordPress versions from 3.7 to 5.3 via a minor release. Automatic updates are enabled by default for minor releases and we strongly recommend that you keep them enabled.

References:

>https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2019-16773


