/* Copyright 2009-2010 Taco Software. All rights reserved.
 * http://tacosw.com
 *
 * This file is part of the Component Library included in Taco HTML Edit.
 * Licensed users of Taco HTML Edit may modify and use this source code 
 * for their web development (including commercial projects), as long as 
 * this copyright notice is retained.
 *
 * The contents of this file may not be published in a format intended
 * for access by other humans, so you may not put code examples on a
 * web site with all or part of the contents of this file, and you may
 * not publish the contents of this file in a printed format.
 */

function tswVideoPlayerInit()
{
	//Browsers that don't support <video> will fallback to Flash automatically.
	if(tswVideoPlayerSupportsVideo())
	{
		//Copy result into array because NodeList can change when DOM changes are made.
		var videos = document.getElementsByTagName('video');
		var videosArray = new Array(videos.length);
		for(var i=0; i<videos.length; i++)
		{
			videosArray[i] = videos[i];
		}
		for(var i=0; i<videosArray.length; i++)
		{
			tswVideoPlayerFallbackToFlashIfNeeded(videosArray[i]);
		}
	}
}

tswUtilsAddEventHandler(window, "load", tswVideoPlayerInit);

function tswVideoPlayerSupportsVideo()
{
	return !!document.createElement('video').canPlayType;
}

function tswVideoPlayerSupportsType(type)
{
	if(!type)
	{
		return false;
	}
	
	var v = document.createElement("video");
	return v.canPlayType(type);
}

function tswVideoPlayerTypeForSource(sourceOrVideoElement)
{
	var type = sourceOrVideoElement.getAttribute('type');
	if(!type)
	{
		var src = sourceOrVideoElement.getAttribute('src');
		if(src)
		{
			ext = src.substring(src.lastIndexOf('.') + 1).toLowerCase();
			
			if(ext == 'ogv')
				type = 'video/ogg';
			else if(ext == 'mpg')
				type = 'video/mpeg';
			else
				type = 'video/' + ext;
		}
	}
	return type;
}

function tswVideoPlayerFallbackToFlashIfNeeded(videoElement)
{
	var flashObjs = videoElement.getElementsByTagName('object');
	if(flashObjs.length == 0)
	{
		return false;
	}
	
	var type = tswVideoPlayerTypeForSource(videoElement);
	if(tswVideoPlayerSupportsType(type))
	{
		return false;
	}
	
	var sources = videoElement.getElementsByTagName('source');
	for(var i=0; i<sources.length; i++)
	{
		type = tswVideoPlayerTypeForSource(sources[i]);
		if(tswVideoPlayerSupportsType(type))
		{
			return false;
		}
	}
	
	//Substitute flash object for video element in DOM
	videoElement.parentNode.replaceChild(flashObjs[0], videoElement);
	
	return true;
}

/* The checksum below is for internal use by Taco HTML Edit, 
   to detect if a component file has been modified.
   TacoHTMLEditChecksum: 68CCF0D5 */