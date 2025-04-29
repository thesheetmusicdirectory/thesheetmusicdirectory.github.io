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

function tswAudioPlayerInit()
{
	//Browsers that don't support <audio> will fallback to Flash automatically.
	if(tswAudioPlayerSupportsAudio())
	{
		//Copy result into array because NodeList can change when DOM changes are made.
		var audios = document.getElementsByTagName('audio');
		var audiosArray = new Array(audios.length);
		for(var i=0; i<audios.length; i++)
		{
			audiosArray[i] = audios[i];
		}
		for(var i=0; i<audiosArray.length; i++)
		{
			tswAudioPlayerFallbackToFlashIfNeeded(audiosArray[i]);
		}
	}
}

tswUtilsAddEventHandler(window, "load", tswAudioPlayerInit);

function tswAudioPlayerSupportsAudio()
{
	return !!document.createElement('audio').canPlayType;
}

function tswAudioPlayerSupportsType(type)
{
	if(!type)
	{
		return false;
	}
	
	var v = document.createElement("audio");
	return v.canPlayType(type);
}

function tswAudioPlayerTypeForSource(sourceOrAudioElement)
{
	var type = sourceOrAudioElement.getAttribute('type');
	if(!type)
	{
		var src = sourceOrAudioElement.getAttribute('src');
		if(src)
		{
			ext = src.substring(src.lastIndexOf('.') + 1).toLowerCase();
			
			if(ext == 'mp3')
				type = 'audio/mpeg';
			else if(ext == 'oga' || ext == 'ogg' || ext == 'ogv' || ext == 'spx')
				type = 'audio/ogg';
			else if(ext == 'm4a' || ext == 'mp4')
				type = 'audio/mp4';
			else
				type = 'audio/' + ext;
		}
	}
	return type;
}

function tswAudioPlayerFallbackToFlashIfNeeded(audioElement)
{
	var flashObjs = audioElement.getElementsByTagName('object');
	if(flashObjs.length == 0)
	{
		return false;
	}
	
	var type = tswAudioPlayerTypeForSource(audioElement);
	if(tswAudioPlayerSupportsType(type))
	{
		return false;
	}
	
	var sources = audioElement.getElementsByTagName('source');
	for(var i=0; i<sources.length; i++)
	{
		type = tswAudioPlayerTypeForSource(sources[i]);
		if(tswAudioPlayerSupportsType(type))
		{
			return false;
		}
	}
	
	//Substitute flash object for audio element in DOM
	audioElement.parentNode.replaceChild(flashObjs[0], audioElement);
	
	return true;
}

/* The checksum below is for internal use by Taco HTML Edit, 
   to detect if a component file has been modified.
   TacoHTMLEditChecksum: 9CFBA480 */