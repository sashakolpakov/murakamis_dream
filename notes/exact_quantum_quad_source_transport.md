# Exact quad transport retains a finite cross-wall sewing source

28 October 2026. There is an exact finite Fourier/chirp transform
of a pointed cyclic source into its positive quad rotation. Its
coefficient is nonzero and polynomially bounded on fixed-log root
trajectories. This alone is not the required global bridge: that
source parameter is a source-flag cross-ratio, and the original
crossing has nilpotent finite-head walls.

Those walls admit a useful global reduction. Each actual two-head
Euler resolvent is a cyclic resolvent plus four explicit sewing
terms. On the original small circle only TWO cross-wall terms
contribute. Thus a word with m crossings has an exact cyclic
comparison with at most `2^(3m)` sewing sectors, retaining the
original caps and peripheral factors. The source-free cyclic
bulk has zero original period. This is a theorem about the
actual source, not a geometric nonvanishing assertion.

## 1. Exact sewing for the literal two-head transfer

Let S be the cyclic unit raising shift on the actual head
`e_0,...,e_(N-1)`, and let `J_+,J_-` be its truncated raising
and lowering shifts. Fix a nonzero marked scalar a. The actual
positive transfer and its cyclic completion are

    T=a J_+ tensor J_-, A=a S tensor S^-1.        (1)

They preserve the total index modulo N. In its residue-k fiber
use `b_n=e_n tensor e_((k-n) mod N)`, `0<=n<N`, and put
`h=k+1`. Then A is a times the cyclic raising shift in n.
The actual T deletes the outgoing edges at n=N-1 and n=k;
if k=N-1 those edges coincide. Its two path lengths are h
and N-h, with the zero-length second path omitted at h=N.

Write `R_A(t)=(tI-A)^-1`, `z=a/t`, and in this fiber put

    U_h=[b_0,b_(h mod N)],
    C_h(z)=[[1,-z^(N-h)],[-z^h,1]].

For EVERY h=1,...,N, exactly

    (tI-T)^-1=R_A-R_A U_h C_h(a/t) U_h^t A R_A. (2)

For h<N this is a rank-two Woodbury formula. Indeed

    I+U_h^t A R_A U_h
       =1/(t^N-a^N) *
         [[t^N,a^(N-h)t^h],[a^h t^(N-h),t^N]],

whose inverse is precisely C_h. For h=N the two columns of
U_h coincide; their total coefficient in (2) is `1-z^N`,
the ordinary single-deleted-edge formula. This separately
checks the overlapping-wall fiber; a rank-two inverse at
coincident columns is not assumed.

There is a global version without an explicit sum of fibers.
Let `V_0,V_1:C^N -> C^N tensor C^N` be

    V_0 e_k=e_0 tensor e_k,
    V_1 e_k=e_((k+1) mod N) tensor e_(N-1),

and let H on their auxiliary head have entry k+1. Expanding
(2) gives the fixed five-term identity

    R_T=R_A-R_A V_0 V_0^t A R_A-R_A V_1 V_1^t A R_A
       +R_A V_0 z^(N-H) V_1^t A R_A
       +R_A V_1 z^H V_0^t A R_A.                (3)

The cyclic central factor is the FULL `A^N=a^N I`; it has
not been reset at an ideal meridian. In the actual crossing
`a=x^-1`, or `Q^-1 x^-1` for the opposite-root u realization.
Both have `a^N=x^-N`, with the original peripheral mark retained.
The negative transfer follows by exchanging the two heads.

## 2. Only cross-wall sewing has the original small-circle period

Let f(t) be any germ holomorphic at zero, in particular either
marked inverse cyclic dilogarithm used in the
[all-inverse original period](actual_whole_word_cyclic_dilog_resolvent_period.md).
Choose the original circle `0<rho<min(1,|a|)`. The cyclic
matrix A is invertible, so R_A is holomorphic inside this
circle. The first three terms of (3) are therefore holomorphic
there after multiplication by f. Their Cauchy periods vanish.
The exact functional calculus reduces to

    f(T)=1/(2pi*i) integral_(|t|=rho) f(t) [
         R_A V_0 (a/t)^(N-H) V_1^t A R_A
        +R_A V_1 (a/t)^H V_0^t A R_A] dt.       (4)

Here `f(T)` means the first N Taylor coefficients evaluated
at the actual nilpotent T. Equation (4) includes f=1, so
the sewing is not merely a correction to higher coefficients.
It supplies the entire identity operator's period as well.

Apply (4) to all `3m` literal transfer Euler slots in the full
`9m`-curve original-word representation. Every other factor,
including the six factorial coefficient functionals per crossing,
Gaussian diagonals and original cap, remains unchanged.
Multilinearity gives an exact sum of at most `2^(3m)` cyclic
cross-wall sewing networks. The auxiliary head of each sewing
map is its existing total-index residue; no number of new
sector types grows with N. Any putative sector containing a
source-free cyclic transfer slot has zero original period.

This gives a genuine whole-network cyclic comparison with the
source retained. It does not identify its kernels with the
standard positive geometric tetrahedron tensor.

The small-circle identity must not be turned into an unmarked
termwise radial-cut identity. Separate R_A factors have poles
at `t^N=a^N`; (2) cancels all of them in the full nilpotent
resolvent. For a simple cyclic eigenvalue, its nonzero spectral
projection is the residue. If such a pole meets a cyclic-D cut
endpoint, separate sewing/bulk pieces can be nonintegrable even
though the full original differential is integrable. Their
relative cycles or matched residue corrections are compulsory.
On `t=a exp(s/N)` the sewing weights have sizes
`exp[-s h/N]` and `exp[-s(1-h/N)]`. For an interior physical
momentum h/N they remain order one, rather than disappearing
as N grows. They are part of the leading source transport.

There is a controlled balancing gauge in this endpoint scale.
Choose one common logarithm of z and set

    B_h=diag(z^((N-2h)/4),z^((2h-N)/4)).

Directly,

    B_h^-1 C_h B_h=[[1,-z^(N/2)],[-z^(N/2),1]]. (4a)

Its Hermitian part is at least `(1-|z|^(N/2))I` for `|z|<1`.
For `|z|=exp(-s/N)`, the condition number of B_h is at most
`exp(s/2)` and this lower bound is `1-exp(-s/2)`, uniformly
in h,N. Thus the sewing matrix has an actual accretive gauge
in the natural endpoint scale. This does not make the full
complex contraction positive or remove its cyclic poles.

Those pole corrections can be seen by the original cap itself.
At N=2,M=1,Q=-1,x=i, the opposite-root u realization has a=i
and the actual Gaussian D is I. Keep the actual fusion C and
the averaged original two-head pivotal cut with pivots `(-i,i)`.
With the original common Cartan factor retained externally,

    Phi(C R_T C^-1)=2i/t^2,
    Phi(C [two cross terms] C^-1)
                   =-2i(t-1)(t+1)/[t^2(t^2+1)^2]. (4b)

The latter has nonzero double-pole coefficient i at BOTH
`t=i` and `t=-i`. These lie off the inverse-D branch cut
`(-infinity,-1]`. Thus the extra cyclic-pole corrections are
source-visible in the actual crossing, rather than artifacts
of an arbitrary matrix probe. The small-circle equality is
exact, but keeping only its old radial branch cuts is false.
Indeed after multiplying by the actual inverse-D function
`f(t)=(1+t)^(-1/2)`, continued from zero, the residues are
`(-9-i)/(4sqrt(1+i))` and `(9-i)/(4sqrt(1-i))`, respectively.
Both are nonzero with their original marks.

The subsequent [regularized cut theorem](cyclic_sewing_regularized_cut_cycle.md)
now carries every sewing sector to a specified cut period: use at most
two endpoint Taylor subtractions at ramified poles, and subtract the
ordinary residues at unramified cyclic poles. Its equivalent differentiated
radial integrals are absolutely convergent. This constructs the matched
cut prescription rather than leaving its regularization unspecified;
the geometric selection and final cancellation estimate remain open.

## 3. An exact Fourier/chirp positive quad transform

Set `q=exp(pi*i/N)`, `Q=q^2`, `gamma=-q`, and define the
unitary matrix

    W_(k,n)=N^(-1/2) gamma^n Q^(kn+n(n+1)/2).    (5)

The chirp is periodic since `gamma^N Q^(N(N+1)/2)=1`, so
(5) works at every parity without division modulo N. With
`Z e_n=Q^n e_n` and the cyclic S above, direct multiplication
gives

    W Z^-1 W^-1=S,
    W Z^-1 S W^-1=gamma Z.                     (6)

For `u^N+v^N=1`, `uv!=0`, put

    p(u,v)_n=Omega(u,v|n)=v^n/(uQ;Q)_n.

All denominators are nonzero, and p spans the one-dimensional
kernel of `1-uZ-vS`. Define

    u'=q v/u, v'=1/u.

Then exactly

    W p(u,v)=c_N(u,v) p(u',v'),
    c_N=N^(-1/2)sum_(n<N)gamma^n Q^(n(n+1)/2)Omega(u,v|n),
    (u')^N=1-1/u^N, (v')^N=1/u^N.              (7)

Indeed the same p is killed by
`1-(-X^-1Y)-X^-1` for `X=uZ,Y=vS`. Equations (6) turn
these operators into `1-u'Z-v'S`. The target kernel has
dimension one by its cyclic first-order recurrence. W is
invertible, so the coefficient c_N is NEVER zero. This proves
nonvanishing directly, rather than assuming it in a Fourier
identity.

The parameters return exactly after three applications. Also

    W^3=omega_N I,
    omega_N=N^(-1/2)sum_(n<N)gamma^n Q^(n(n+1)/2),
    |omega_N|=1.                               (8)

To prove this, conjugation (6) has order three on Z,S, hence
W^3 is scalar. Its (0,0) entry is the displayed sum, since
the product of chirps at a,b times Q^(ab) is the chirp at
a+b modulo N. Unitarity proves its modulus. Consequently
the three coefficients c_N multiply to the retained omega_N,
not an independently chosen scalar one.

## 4. Polynomial source coefficient and exact cap transport

Let the compatible logarithms of `u^N` and `v^N` remain in
fixed compact sets, with their central values away from zero
and one, and
`u=exp(w/N),v=exp(s/N)`. Uniformly for every `0<=n<N`,

    N^-C <= |Omega(u,v|n)| / |1/(Q;Q)_n| <= N^C. (9)

For a direct proof compare each denominator to `1-Q^j`.
Away from a fixed number of endpoint indices its relative
change is `O(1/min(j,N-j))`; the logarithms sum to `O(log N)`.
At the finitely many endpoints the ratios tend to nonzero
values proportional to `w+2pi*i*j` or `w-2pi*i*j`. Compactness
and `exp(w)!=1` bound these above and below. The numerator
`|v|^n` is bounded by fixed constants. The same estimate holds
for the transformed marks
`w'=pi*i+s-w`, `s'=-w`. Since W is unitary, (7) therefore gives

    N^-C' <= |c_N(u,v)| <= N^C'.                 (10)

These are actual uniform upper/lower bounds for the selected
local source coefficient. They concern fixed-log root paths;
they do not identify central and semiclassical shape coordinates.

All caps and tensor compositions have an exact transport rule.
For any actual column p, row ell, pairing M and tensor R, use

    p'=Wp, ell'=ell W^-1,
    M'=(W_left^-1)^t M W_right^-1,
    R'=(tensor W_out) R (tensor W_in)^-1.        (11)

Every contracted inverse pair cancels, preserving the entire
original scalar, not just a unit vector. If a pointed fusion
maps `p_A tensor p_B` to `p_C tensor p_D`, its transformed
tensor maps the normalized target quad units with the exact
factor `c_C c_D/(c_A c_B)`. This nonzero scalar must be kept
or carried by the boundary rows. It is not reset to one.
The same basis changes transport V_0,V_1 and their dual rows
in (3)-(4), preserving all cross-wall sewing exactly.

## 5. Why this is not yet the geometric quad bridge

In the existing shared-face frame, the ACTUAL raw unit maps
to `p(rho_f,a_f)`, since `G_f 1=(phi_f(n)^-1)_n`.
But its central parameter is the source-flag cross-ratio

    t_f(s)=(p_j-s)(p_i-p_k)/((p_i-s)(p_j-p_k)),

not the tetrahedral shape. Equation (7) is exactly cyclic
ordering of that face with its source flag retained. Its
Gaussian matrix is consequently compatible with the previous
shared-face cyclic matrices; naming it a Fourier transform
does not supply a new tetrahedron identification.

This distinction is generic. Normalize four geometric flags
to `(infinity,0,1,z)` and use the standard tetrahedron shape
`w=1/z`. Two source-face parameters are

    t_B(s)=s, t_A(s)=w(1-s)/(w-1).

Requiring both to lie in the positive quad orbit
`{w,1-1/w,1/(1-w)}` forces w to be a root of one of

    w^2+w-1, w^2-w-1, w^2-3w+1, 3w^2-3w+1.      (12)

This follows by substituting the three possible values of s
in the second formula and comparing with the same three
values. In the upper half-plane only
`w=1/2+i/(2sqrt(3))` survives this necessary condition.
Thus for every other positive tetrahedron no common source
flag makes even these two face-unit parameters its positive
quads. This rules out that specific facewise identification;
it does not rule out a genuine four-leg geometric transform.

There is also an all-N actual-source obstruction to omitting
the nilpotent wall. On one head write
`J_+=(I-|0><0|)S`, `A=W S W^-1`. Since W's zeroth column
is constant,

    W J_+ W^-1=(I-P)A, P=J_allones/N.           (13)

For the original fixed cap `p=e_0`, `ell=allones`, retain
`p'=Wp,ell'=ell W^-1`. Then `ell' P p'=1`; the original
averaged cut evaluates the transported projector as `1/N`.
The wall is a specified, source-visible operator at every N.
It cannot be declared negligible solely from a nonzero generic
cyclic coefficient or a metaplectic basis change.

The viable remaining route is therefore precise: carry the
finite cross-wall sewing sectors (4), their matched cycles,
and the transformed caps (11) into the positive geometric
kernel. Equations (7)-(10) control a real local source transport;
they do not prove that the whole original cut cycle has a
nonzero geometric intersection. That global lower bound
remains unproved.

[Exact audit](../experiments/audit_exact_quantum_quad_source_transport.py).
It checks (2)-(4), the all-level Fourier identities, the retained
caps and whole actual signed words, and the polynomial equations
in (12). The uniform proofs above do not rely on finite examples.
