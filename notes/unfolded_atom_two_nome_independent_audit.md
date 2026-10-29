# Independent audit of the whole Ward atom and its two-nome completion

27 October 2026. Independent proof pass of
[the cyclotomic-divisor and two-nome construction](unfolded_atom_cyclotomic_divisors_and_two_nome_source.md),
especially Sections 2, 3, 5 and 6. The fixed-level sectorial nature
of the assertions is necessary and is stated in that note. This audit
does not promote its finite root formula to an ordinary meromorphic
parameter germ, a whole selected-knot source, or a volume theorem.

## 1. Fixed-level sectorial expansions and the normal-slope norm

For a fixed primitive n-th root, split the absolutely convergent
logarithm sum into m divisible by n and its complement. In a closed
negative-real epsilon sector the nonresonant denominators have a
uniform positive bound: for m times absolute epsilon small this is
the finite root separation, and for it large the radial modulus is
bounded below. Their differences from the root value are bounded
by a constant times m times absolute epsilon. For the resonant
terms the bound

\[
 \left|\frac1{1-e^u}+\frac1u-\frac12\right|\leq C|u|
\]

holds on that sector, using its Taylor expansion near zero and
radial bounds outside a disk. Geometric decay in z then sums the
errors. This proves the displayed O(epsilon) estimate uniformly
on |z| at most r less than one, with n fixed. Its constant may
depend on n; it does not give an estimate for growing n.

Putting U=exp(t n epsilon), each resonant term of the log ratio
has limit -t z^(kn)/k. The nonresonant difference is O(epsilon).
Uniformity for compact t follows after absorbing exp(C m absolute
epsilon) into a slightly larger z disk. Thus the exceptional value
is exactly (1-z^n)^t with its z=0 mark. At t=1 the actual identity
F(Q,zQ^n)/F(Q,z)=(z;Q)_n proves its norm interpretation without an
interchange of two limits. The rational-slope telescope uses its
different shifted arguments; it is not an off-exceptional identity
claiming that the first ratio raised to a power is that product.

## 2. The root completion constants, including the source half-power

Write c=2 pi i, H=c/N+epsilon, X=exp(Nx), V=Log(1-X). Direct
inversion, not an asymptotic approximation, gives

\[
 \widetilde H=4\pi^2/H+cN,\quad
 \frac1{\widetilde H}=\frac1{N^2\epsilon}+\frac1{cN},\quad
 w=X\exp(\gamma\widetilde H),\quad \gamma=1-x/c.
\]

The first-nome constant after its polar term is log D_N minus V/2.
The dual n=1 atom has constant -Li_2(X)/(cN)+(gamma-1/2)V.
Subtracting these two constants cancels their entire simple polar
asymptotic term and gives

\[
 \Psi_N=D_N\exp(\operatorname{Li}_2(X)/(cN))(1-X)^{x/c-1}.
\]

With nu=(1-X)^(1/N), g_D=D_N/nu^((N-1)/2) and
S=Li_2(X)+(Nx)V this is precisely

\[
                 \Psi_N=g_D\exp(S/(cN))\nu^{-(N+1)/2}.
\]

Both half-power factors are required: their combined exponent is
-N on nu, producing the factor (1-X) inverse in the preceding
formula. The first shift x to x+c/N changes S by cV and changes
g_D by (1-z)/nu, which combine to the original Ward multiplier
1-z. The second shift x to x+c gives the multiplier 1-X. All
these signs and the original central norm 1-X pass independently.
The stated conclusion is the radial/sectorial fixed-N value; the
calculation alone does not prove holomorphic extension around a
whole root neighborhood.

## 3. Exact accumulating zeros are a decisive parameter obstruction

For fixed real x less than zero, put H_k=(x-c)/k. Its real part is
negative, so both infinite products in the actual defining ratio
converge. Since 4 pi squared plus 2 pi i x equals c(x-c), one has
w(H_k)=exp(ck)=1. Only the numerator factor 1-w vanishes: every
remaining numerator factor is 1-Qtilde^j with modulus of Qtilde
less than one, and the denominator has modulus of z and Q less
than one. The derivative of w at H_k is nonzero. These are
therefore exact simple zeros, accumulating at H=0 inside its
product domain.

A nonzero horizontal solution of a meromorphic rank-one connection
at zero is nonzero at every sufficiently small nonzero ordinary
point, by uniqueness of its scalar differential equation. Such a
solution cannot have these zeros. A finite algebraic ramification
and a fixed nonzero Puiseux meromorphic gauge do not remove them.
The uncompleted atom already has accumulating nonzero cyclotomic
exponential singularities. These two explicit facts forbid an
automatic ordinary meromorphic-line interpretation of either atom.
They do not prohibit cancellations in a fully specified word/source.

## 4. The physical-root leading estimate has the stated sign

For g(t)=t Log(1-z exp(ct)), elementary trapezoid summation gives
sum_(j=1)^(N-1) g(j/N)=N integral_0^1 g-(g(0)+g(1))/2+O(1/N).
Termwise integration on |z| less than one gives integral g=-Li_2(z)/c.
Thus log D_N=-Li_2(z)/H_N-Log(1-z)/2+O(1/N), uniformly on a
fixed marked compact z chart. The remaining logarithm in the exact
completion formula is exponentially small there because X=z^N.
The note's physical-root estimate follows with its negative
one-half logarithmic term. It does not supply a selected geometric
knot period or a uniform estimate across the accumulating divisors.
