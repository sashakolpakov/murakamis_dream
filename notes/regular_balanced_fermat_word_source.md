# Regular balanced Fourier blocks with the original whole knot source

28 October 2026. The original complete Kashaev state admits an exact
whole-word presentation by regular, fully balanced full-Psi crossing
blocks. Independent local Fermat parameters avoid the collision that
would result from matching the same central grid along a closed knot.
The finite Fourier changes between those local grids and the original
caps are retained explicitly; their norms and inverse norms are
bounded independently of level for fixed nonzero central parameters.

This is a source theorem for arbitrary signed words and bridge count,
not a new positive invariant. The remaining relative-source problem is
now in a specified network of full-Psi blocks and rational Fourier
gluing kernels. Their scalar geometric pairing is not determined by
the norm bounds alone.

## 1. Balancing is an actual quadrature operation

Use the exact [complete crossing layer](actual_trivalent_layer_crossing_source.md)
and put N>=2, d=N-1, q=exp(pi*i/N), Q=q^2, x=-q^(-1),
s=x^N=(-1)^(N+1). For a positive crossing its raw kernel is

    K(t)=B_N(t/z1,x^-1 t/z0)
          R_N(z6/z0,x^-1 z6/t)
          B_N(x^-1 z7/z6,x^-2 z7/t).                 (1)

The original scalar kappa is outside (1) throughout. Write the
external central coordinates as

    A=z0^N, B=z1^N, C=z6^N, D=z7^N.

First choose the ADAPTIVE internal sampling orbit t_j=t0 Q^j with

    t0^(-N)=B^(-1)-D^(-1).                          (2)

The exact physical crossing is unchanged by this operation. Indeed
K has t-exponents in [-2d,d], so its orbit average differs from its
constant term only by

    (z1^(-N)-z7^(-N)) [t^(-N)] K.                   (3)

Every coefficient of K has nonpositive z1 exponent and z7 exponent
between zero and d. The first term in (3) demands second input index
at least N; the second has negative second output index. The actual
finite physical boundary windows kill both, separately. This proof
uses input and output windows rather than treating projection as a
multiplicative quotient.

On (2) the one-function Fourier closure character is exactly one.
It is legitimate here because t0 was changed BEFORE projecting the
complete finite kernel. For fixed scalar t0 the statement would be
false: the same physical windows instead kill the closure character
times the complete kernel. The two operations are different.

The full symmetric orbit average is CT K plus (3), so it extends
rationally even at B=D where the individual sampling points escape.
We will choose regular parameters below, so that no such escape is
needed in this presentation.

## 2. A regular local Fermat multisection kills all three local norms

Choose fixed nonzero complex numbers A,B with B!=s A. Choose marked
roots r0^N=A, r1^N=B, and set

    r6=x r1, r7=x r0,
    C=s B, D=s A,
    T=t0^N=B D/(D-B).                               (4)

Evaluate each external port on its N-point grid r_i Q^k, and use
the internal orbit (2). None of these roots is set to an unspecified
ideal-point value. The exact three source norms in (1) become

    1-T/B+s T/A=0,
    1-C/A-s C/T=0,
    1-s D/C+D/T=0.                                 (5)

Here s^2=1 is the COMPLETE-color identity, retained also at even N.
Thus all THREE finite Newton/Rogers kernels equal their specified
homogeneous full-Psi sections at every sampling point. This is an
identity of the whole finite kernel on a regular multisection, not a
rule discarding individual currents under a raw source quotient.

The [local balanced Fourier block](actual_balanced_fourier_crossing_kernel.md)
then uses the exact one-Psi orbit evaluation to remove the internal
orbit. The result is a specified four-full-Psi kernel, with its actual
Gaussian, Cartan, affine logarithmic marks and central norm factors.
There is no unknown periodic normalizer. The regular balanced
reference coefficient is nonzero.

For a concrete choice valid for EVERY parity take A=2, B=3i. Then
B!=s A, all quantities in (4) are finite and nonzero, and the
balanced arguments and their complements are nonzero. The marked
full functions are continued together; no logarithm is silently
reduced modulo 2*pi*i.

## 3. Inverse Fourier reconstruction gives the EXACT original operator

Define the normalized one-head Fourier matrix

    F(r)_(k,a)=N^(-1/2)(r Q^k)^a, 0<=k,a<N.          (6)

Let F_in=F(r0) tensor F(r1), F_out=F(r6) tensor F(r7).
The balanced grid block is

    B_N(k6,k7;k0,k1)=kappa/N^2
                          * (1/N) sum_j K(t0 Q^j).   (7)

All external variables in (7) are their indicated grid values. The
two factors 1/N from the two-head Fourier transform and its inverse
are responsible for N^(-2); the internal orbit contributes N^(-1).
Replacing K by its balanced full-Psi expression changes nothing in
(7). Define its reconstruction in ORIGINAL indices by

    Rhat=F_out^(-1) B_N F_in.                         (8)

The local theorem proves Rhat-R has only total INTEGER degree
increment +N. Here is the support argument, independent of level or
numerical tests. A raw term has input (a,b), output (c,e) with

    0<=a<=2d, 0<=b,e<=d, -d<=c<=d,
    c+e-a-b=-(t exponent).                          (9)

Internal quadrature retains t exponent 0 or -N. For exponent zero,
an external Fourier alias can only fold a>=N down by N, or c<0 up
by N. Each operation raises output minus input degree by N. They
cannot occur together under degree conservation and b,e<=d.
For exponent -N the term already has increment +N. Its degree and
the bounds in (9) force a<N and c>=0, so no external alias occurs.
All other terms are the original physical block. This proves the
claimed error grading with all Fourier radius factors retained.

There is a stronger exact conclusion. The local four-function kernel
satisfies the ORIGINAL lowering-current identity for

    Ecal|a>=(Q^(-a)-1)|a-1>,
    K|a>=x Q^(-a)|a>, E_total=Ecal_1 K_2+Ecal_2.

This follows from four exact full-Psi h-shift ratios and their rational
Ward identity, with the finite Fourier endpoint coefficients retained;
the complete proof is Section 5 of the local kernel note. In particular
[Rhat,E_total]=[R,E_total]=0. E_total is injective on every total-degree
block t>=N: its rectangular bidiagonal matrix has a nonzero extreme
coefficient, which forces the first input coefficient to vanish, then
the next, through the whole block.

Put Delta=Rhat-R. Its degree is +N by (9). On input degree zero,
E_total Delta=Delta E_total=0, so injectivity on degree N gives Delta=0.
Induction on input degree j gives the same conclusion on degree j+N.
At j>=N-1 that output degree exceeds 2d and Delta is already zero.
Therefore, for EVERY level,

    Rhat=R,  Rhat^(-1)=R^(-1).                       (10)

The formerly allowed aliases cancel exactly. This is a literal
operator theorem, not just equality after a chosen knot contraction.

For a negative crossing use the proved COMPLETE-color identity
R_-=P overline(R_+)P, transporting the whole regular balanced block,
its frames and kappa. Complex conjugation of (6) is another matrix
of the same kind with the grid permutation k->-k. Such permutations
and the port flip are retained. The negative reconstruction is
therefore exactly R_- as well.
This does not delete the continuous Gaussian in a separately
sampled raw negative sector; it transports the ENTIRE positive
identity, which already includes its original normalization.

## 4. Whole signed words and the original source

For ANY signed word W on ANY number of physical heads, composition of
the exact identities (10) gives

    What=W,                                        (11)
    original_source(What)=original_source(W).       (12)

All original inserted operators and currents at this fixed complete
root may be transported by the same Fourier frames, including operators
that lower degree. This stronger assertion is justified by (10), not
by applying the earlier positive-degree source argument outside its
scope. Braid identities and inverse identities are consequently exact.

In particular the whole original one-cut matrix and the original
pointed-plat scalar are retained, with all cups, ordinary caps, the
FULL marked row, pivots and external normalization. No standalone new
operator invariant or positive state is substituted.

This theorem is at the COMPLETE color M=1 and fixed root. It does not
identify generic-meridian derivatives or off-root quantum-normal jets;
those require their own continuation identity. Transporting an
already specified finite operator at M=1 is different from proving an
identity of its unsupplied off-root germ.

## 5. Independent grids are joined by explicit bounded adapters

Using the SAME central grid on a whole closed knot would in general
invalidate regularity in (4). Indeed center exchange is
(A,B)->(sB,sA). These are signed permutations, conjugate to ordinary
adjacent permutations by the alternating diagonal s^(j-1). For a
one-component braid closure the matched center vector is fixed by
its one-cycle permutation. At every crossing it then has B=sA,
so D=B and T=infinity. We avoid this collision by retaining the
exact basis transitions between INDEPENDENT regular local choices.

If a wire goes from root r to the next root r', its adapter is

    E(r',r)=F(r')F(r)^(-1),
    E_(j,k)=(1/N)sum_(a=0)^d (r'/r)^a Q^((j-k)a)
           =[1-(r'/r)^N]/[N(1-(r'/r)Q^(j-k))].       (14)

At a removable collision use the finite sum. All marked root phases
and the associated grid permutations remain. Pivot insertions are
conjugated in the same manner, rather than dropped from (14).
Initial cups become F_in p and final rows become m F_out^(-1),
using their actual full coefficients. Expanding this network
recovers exactly the original-index composition of (8), hence (12).

Choose r=exp(Log A/N) times a retained unit phase, for a fixed
nonzero central A. Unitarity of the normalized root Fourier matrix
gives the exact bounds

    ||F(r)|| <= max(1,|A|),
    ||F(r)^(-1)|| <= max(1,|A|^(-1)).                 (15)

Thus every adapter and its inverse is uniformly bounded in N for
fixed regular choices from a finite parameter list. The actual cap
normalizations remain polynomial in N. In particular choosing
A=2, B=3i separately at each positive crossing, and their transported
conjugates at negative crossings, creates no hidden exponential
normalization cost. Roots are specified before the finite sums;
no coefficient depending on the unknown knot value is chosen.

## 6. What this source theorem accomplishes and what remains

There is now an exact general source presentation with REGULAR
balanced full-Psi blocks, for both signs, and all local B/R currents
eliminated at those sampling points by the actual equations (5).
It uses a proved quadrature/polarization map and the actual lowering
Ward identity, not a raw balanced quotient of finite heads.
This is a stronger comparison than merely normalizing a candidate
geometric section or bounding its normal image.

The adapters in (14) must stay. For distinct fixed central centers
and fixed nonzero angular separation they are generally O(1/N),
not exponentially small. Their norm bound does not authorize
replacing them by identity wires or neglecting their endpoint
tails. Matching the grids to remove them would return to the cusp
collision above. Thus the remaining global relative source is
explicit, but its geometric coefficient and other scalar sectors
still require analysis. No broad volume limit is inferred from
the exact balanced presentation alone.
