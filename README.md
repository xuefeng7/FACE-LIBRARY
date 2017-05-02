# FACE-LIBRARY
This repository contains 690,269 analyzed faces obtained from Instagram posts. We have included the face attributes(age, gender, race, and etc.) and facial landmarks for each of these faces. 
# Goal
Instagram is a rich source for high-quality images, we believe those images can be tremendously helpful to the research community; however, Instagram restricts its API accesses to company only, and it builds many barricades for web crawlers. Thus, we decide to share the Instagram posts we retrieved. Further and more importantly, since detecting faces can cost numerous time and computing power, we share all those processed faces with the hope of saving time and efforts, facilitating the research for whom may concern.  
## Timeline post
We collected all faces from all acquired posts. We also recorded the timestamp, user_id, and post_id for each post, so that one can retrieve post from Instagram easily.
## Face detection (powered by Face++)
For each face, the included attributes are age, gender, race, and smiling. Along with face width and height, five facial landmarks are provided. They are eye_left, eye_right, nose, mouth_left, mouth_right, and center. The following figure illustrates the facial landmarks.

<img src="https://github.com/xuefeng7/FACE-LIBRARY/blob/master/figures/landmarks.jpg" width="180">

## Example
The following is one face example in JSON format. **Note that one post may contain more than one face**. 
```json
{
  	"timestamp": "1482223780",
  	"resp": [{
  		"attribute": {
  			"gender": {
  				"confidence": 77.270200000000003,
  				"value": "Male"
  			},
  			"age": {
  				"range": 6,
  				"value": 21
  			},
  			"race": {
  				"confidence": 54.615700000000004,
  				"value": "Asian"
  			},
  			"smiling": {
  				"value": 10.914
  			}
  		},
  		"face_id": "de7ff248bc19cb34e610070f21ee6210",
  		"tag": "",
  		"position": {
  			"eye_left": {
  				"y": 32.795499999999997,
  				"x": 54.653333000000003
  			},
  			"center": {
  				"y": 43.25,
  				"x": 57.416666999999997
  			},
  			"width": 29.833333,
  			"mouth_left": {
  				"y": 51.423499999999997,
  				"x": 48.733333000000002
  			},
  			"height": 29.833333,
  			"mouth_right": {
  				"y": 49.200000000000003,
  				"x": 58.359833000000002
  			},
  			"nose": {
  				"y": 42.856332999999999,
  				"x": 58.156999999999996
  			},
  			"eye_right": {
  				"y": 40.310833000000002,
  				"x": 66.170833000000002
  			}
  		}
  	}],
  	"uid_pid": "3040732185_1409317677457159168.jpg"
  }
```
For the above post, only one face is detected, and the uid is _3040732185_, and pid is _1409317677457159168_.
## How to retrieve post
We can retrive Instagram post via *pid*; however, Instagram does not explicitly utilize *pid* to represent a link to a specific image, instead it utilizes shortcode. Generating shortcode from *pid* requires more work. [Here](http://carrot.is/coding/instagram-ids) is a detailed explaination about the logic behind how to construct shortcode. But we have included a complimentary converter (id2code.py) in this repository. Simply call
```python
  python id2code.py 1467331451728886737 (or your own pid)
```
you will get the short code
```python
  'BRdAi5cDvvR'
```
If you want the post directly, there is a function named *generateUrl* for help. Given pid, the full url points to the image post will be returned.
```python
  'https://scontent-ord1-1.cdninstagram.com/t51.2885-15/s640x640/sh0.08/e35/17077495_255710568218080_4361264754778439680_n.jpg'
```
### A full post retrieving example
As mentioned above, first running
```python
  python id2code.py 1467331451728886737
```
and, we can get the post's short-code, and the post's media address, where you can obtain the image directly.
```python
   'BRdAi5cDvvR' # short-code
   'https://scontent-ort2-1.cdninstagram.com/t51.2885 15/s640x640/sh0.08/e35/17077495_255710568218080_4361264754778439680_n.jpg' # image address
```
Then, with the image address, you can either view the image through the browser, or use any code to download it to your disk, and etc.

