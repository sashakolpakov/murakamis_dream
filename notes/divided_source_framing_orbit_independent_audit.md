# Independent audit of the divided-source framing orbit

Audit, 27 October 2026, of
[the explicit framing-orbit note](divided_source_framing_orbit.md).
The group/sign-cover, density, cyclic-source gauge and marked-anchor
claims are correct in their stated domains. None identifies this
orbit with the internal framing of the knot network.

The actual divided Ward block is standard SL2 in the ordered basis
Ubar,W: the rescalings give eW=Ubar, fUbar=W, and both opposite
actions zero. The cut covector is (1,1)/N. For z=a+b!=0,

    g_v=[a+1/z a;b-1/z b]

has determinant one, carries W to v, and multiplies that covector
by z. These equations determine its first column uniquely, proving
free transitivity rather than only matching dimensions.

The contragredient is essential. Since (1,1)g=z(1,1), the matrix
j(g)=z g^(-T) has row sums one. It is a homomorphism with kernel
{+I,-I}. Conversely a row-stochastic invertible matrix has two
preimages after choosing the square root of its determinant.
Thus this is exactly the retained SL2 sign cover. The inverse
right-frame action gives

    F_0 j(g_v)^(-1)=[a/z b/z;z^(-2) -z^(-2)].

The opposite choice F_0j(g_v) would not have the asserted action
convention. With r=a/z and s=z^(-2), direct differentiation gives

    -dr wedge ds/[s(1+s)]=2 da wedge db/(1+z^2).

The source matrices -xi_i^T give the two vector fields in the
note. Their ordinary coordinate divergence is zero, while
X_i(z)=-z, so their divergence in this density is
2z^2/(1+z^2)=2A_src. This matches the actual leading co-source
sign. Also tau=a z and V=z^(-1)(partial_a-partial_b) obey
Vtau=1, VA_src=0, and contraction with the density gives
dlog A_src. The stated relative transgression is therefore exact.

For the matrix comparison, D_j=P_j/c^j sends each upper edge
epsilon_(j+1) to c. Its wrap sends mu to mu P_(N-1)/c^(N-1)=b.
Hence D E_mu D^(-1)=v. The clock commutes with D, so the original
Casimir identity fixes Ftilde in the stated order
(-2-qK-q^(-1)K^(-1))v^(-1). Its N-th power is zero because
it is conjugate to the actual truncated F. This gauge requires
a,b!=0, as explicitly stated; the whole source orbit only requires
z!=0 and is larger than that companion chart.

The normalized coupon is literally

    e_v=(N/z)v e,

whose first N-1 rows are r/(N-1) and last row is 1-r. Thus its
entire response on arbitrary matrices depends only on r. For
the split Ward contraction h delta=I-i p, p=Tr/N, the difference
between its row and the original row vanishes on I. Therefore
(Phi_v-Phi)h delta=Phi_v-Phi; the stated cochain homotopy is valid.
This proves neither equality on arbitrary matrix insertions nor
an internal two-coordinate source map.

At r=(N-1)/N one has v=(z/N)S, S=U+W. The exact permutation
identities are S^N=I, Se=e and e=(1/N)sum_j S^j. The first
condition on v alone permits z/N in mu_N. Its marked eigenvalue
one on e forces z/N=1. Thus the extra clock/eigenvalue mark
really restores z=N; normalized coupon data alone cannot do so.
Substitution gives precisely r=1-1/N, s=1/N^2,
A=N^2/(N^2+1), tau=N(N-1), and mu=1/[(-1)^(N-1)N].

Independent exact checks verified the sign-cover matrix, form and
vertical current symbolically, and S^N, Se and the full projector
identity at eleven integer levels N=2,...,12. The proof arguments
above establish the general statements. The physical 2pi*i
polarization factor and the pre-collapse network source comparison
remain outside these conclusions, as the note correctly records.
