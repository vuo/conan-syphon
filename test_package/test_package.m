// Clang 5 doesn't understand the macOS 11 SDK's availability macros; replace them with our own simpler ones.
#define __OS_AVAILABILITY__
#define API_AVAILABLE(...)
#define API_UNAVAILABLE(...)
#define API_UNAVAILABLE_BEGIN(...)
#define API_UNAVAILABLE_END
#define API_DEPRECATED(message, ...) __attribute__((deprecated(message)))
#define API_DEPRECATED_WITH_REPLACEMENT(replacement, ...) __attribute__((deprecated("Deprecated; repaced by " replacement)))

#include <stdio.h>
#import <Syphon/Syphon.h>

int main()
{
	SyphonServerDirectory *ssd = SyphonServerDirectory.sharedDirectory;
	if (!ssd || !ssd.servers)
	{
		printf("Unable to initialize Syphon.\n");
		return -1;
	}

	printf("Successfully initialized Syphon.\n");

	return 0;
}
