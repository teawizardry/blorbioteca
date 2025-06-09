import { eleventyImageTransformPlugin } from "@11ty/eleventy-img";
import markdownIt from "markdown-it";
import { full as emoji } from 'markdown-it-emoji'
import footnote from 'markdown-it-footnote'
import container from 'markdown-it-container'
import linkAttributes from 'markdown-it-link-attributes'
import multimdTable from 'markdown-it-multimd-table'
import katex from '@vscode/markdown-it-katex'

export default function(eleventyConfig) {
	eleventyConfig.addPlugin(eleventyImageTransformPlugin, {
		formats: ["webp", "gif"],
		sharpOptions: {
		    animated: true,
		}
	});

	let md = new markdownIt({
		html: true,
		breaks: true,
		linkify: true,
		quotes: '“”‘’',
	});
	md.use(emoji, {
		shortcuts: {},
	});
	md.use(footnote);
	md.use(container, 'closed', {

	  validate: function(params) {
	    return params.trim().match(/^closed\s+(.*)$/);
	  },

	  render: function (tokens, idx) {
	    var m = tokens[idx].info.trim().match(/^closed\s+(.*)$/);

	    if (tokens[idx].nesting === 1) {
	      // opening tag
	      return '<details><summary>' + md.utils.escapeHtml(m[1]) + '</summary>\n';

	    } else {
	      // closing tag
	      return '</details>\n';
	    }
	  }
	});
	md.use(container, 'opened', {

	  validate: function(params) {
	    return params.trim().match(/^opened\s+(.*)$/);
	  },

	  render: function (tokens, idx) {
	    var m = tokens[idx].info.trim().match(/^opened\s+(.*)$/);

	    if (tokens[idx].nesting === 1) {
	      // opening tag
	      return '<details open><summary>' + md.utils.escapeHtml(m[1]) + '</summary>\n';

	    } else {
	      // closing tag
	      return '</details>\n';
	    }
	  }
	});
	md.use(linkAttributes, {
	  attrs: {
	    target: "_blank",
	    rel: "noopener",
	  },
	});
	md.use(multimdTable, {
              multiline:  true,
              rowspan:    true,
              headerless: true,
              multibody:  true,
              aotolabel:  true,
        });
	md.use(katex.default);

	// Watch CSS files
	eleventyConfig.addWatchTarget("css/**/*.css");
	// Watch images for the image pipeline.
	eleventyConfig.addWatchTarget("content/**/*.{svg,webp,png,jpg,jpeg,gif}");

	eleventyConfig.setLibrary("md", md);
	eleventyConfig.setDataDirectory("./character_images/");
	eleventyConfig.addCollection("characters", function (collectionAPI) {
		return collectionAPI.getFilteredByGlob("./characters/*.md");
	});
};

export const config = {
	templateFormats: [
		"md",
		"njk",
		"html",
		"liquid",
		"11ty.js",
	],
	markdownTemplateEngine: "njk",
	htmlTemplateEngine: "njk",
};
