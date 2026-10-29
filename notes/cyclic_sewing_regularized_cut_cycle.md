# The actual cyclic sewing has a canonical regularized cut cycle

28 October 2026. The exact two-head cyclic sewing comparison introduces
additional poles which do survive the ORIGINAL source. This note carries
those terms to the original cyclic-dilogarithm cuts without dropping them.
At a ramified endpoint only two Taylor subtraction terms are needed;
equivalently, at most two ordinary derivatives make its radial integral
absolutely convergent. Unramified cyclic poles contribute their specified
residues. The prescription applies entry by entry and through the whole
original ordered word.

This is an exact comparison of selected periods, including their boundary
terms. It is not a positivity theorem or a geometric lower bound. In
particular the positive radial symbol of the unsplit resolvent does not
automatically apply separately to these differentiated sewing terms.

## 1. The actual additional divisor

On a total-index residue fibre, the actual two-head transfer is a cyclic
shift with one or two edges removed. Write its cyclic completion as
`A=a S`, where `S^N=I` and `a=x^-1`, or `a=Q^-1 x^-1` for the opposite-root
realization of an original u factor. Its cyclic resolvent is

    R_A(t)=(tI-A)^-1.

The exact two-cut Woodbury comparison has a sewing matrix

    C_h(t)=[[1,-(a/t)^(N-h)],[-(a/t)^h,1]], 1<=h<=N.

The `h=N` case uses the same cut column twice and reduces to the one-cut
identity. The pure cyclic and the two diagonal sewing terms are analytic
at zero and have zero original small-circle functional-calculus period.
The remaining two cross terms contain two copies of `R_A` and negative
powers of t. Thus their only new nonzero finite poles lie at

    t^N=a^N,                                      (1)

with order at most two in each integration variable. They decay at
infinity. The original nilpotent resolvent has no such poles: their
cancellation belongs to the complete sewing identity.

At completeness `x=-q^-1`, so both realizations retain EXACTLY

    a^N=(-1)^(N+1).                               (2)

For odd N, (1) meets every finite dilogarithm branch point, with the
additional unramified point t=1. For even N its points are interlaced
with the Nth roots. Away from completeness the full factor
`a^N=(-1)^(N+1) M^-N` is retained. No replacement by a numerical scalar
before taking the source is justified. The theorem below uses the unit
circle case, in particular the complete point; small-circle sewing
itself is an identity in the full meridian parameter.

## 2. One-variable regularized Hankel theorem

Fix `Q=exp(2 pi i/N)`, epsilon in {1,-1}, and the original marked branch

    A_epsilon(t)=product_(k=1)^(N-1)
                              (1-Q^(epsilon k)t)^(-k/N),
    A_epsilon(0)=1.

Let B(t) be a scalar or matrix rational function with poles only at zero
and finitely many points of the unit circle, each nonzero pole of order
at most two, and with B(t)=O(t^-1) at infinity. Let Gamma_0 be a sufficiently
small positive circle, lifted to the marked sheet. Put

    alpha_j=Q^(-epsilon j), u_j=j/N,
    g_j(r)=product_(k!=j,1<=k<N)
                           (1-r Q^[epsilon(k-j)])^(-k/N).

Every logarithm has the radial continuation already specified for the
original cut. Let Z be the unramified poles of B, excluding zero. Then

    (1/(2 pi i)) integral_(Gamma_0) A_epsilon(t) B(t) dt
       =sum_(j=1)^(N-1) sin(pi u_j)/pi
           FP integral_1^infinity
                alpha_j (r-1)^(-u_j) g_j(r) B(alpha_j r) dr
         -sum_(beta in Z) Res_(t=beta) A_epsilon(t) B(t) dt. (3)

If B is regular at a branch endpoint, FP is the ordinary convergent
integral. At a pole alpha_j, write x=r-1 and the Laurent germ

    f_j(x)=alpha_j g_j(1+x) B(alpha_j(1+x))
          =b_(-2)x^-2+b_(-1)x^-1+O(1),           (4)

with a missing coefficient set to zero. Its finite part means EXACTLY

    integral_0^1 x^-u [f_j(x)-b_(-2)x^-2-b_(-1)x^-1] dx
      +integral_1^infinity x^-u f_j(x) dx
      -b_(-2)/(u+1)-b_(-1)/u.                   (5)

Both integrals in (5) converge absolutely. This formula fixes the
subtraction convention; there is no adjustable finite constant. The
numbers 1/u and 1/(u+1) are retained. In particular the former can grow
with N at small cut labels.

### Proof and signs

Deform the original small circle within the marked cut plane. The
outer arcs tend to zero because `A_epsilon=O(|t|^(-(N-1)/2))` and
B=O(t^-1). As in the original Hankel proof, this is a sectorwise
deformation and does not assume that the entire outer circle has a
closed lift at even N. The two radial banks have difference

    2i sin(pi u_j) (r-1)^(-u_j) g_j(r).

The factor dt contributes alpha_j dr, giving the first term in (3).
Ordinary positively oriented circles about additional unramified poles
are moved to the other side of the contour identity, giving the MINUS
sign in its residue term.

Near a ramified endpoint, integrate each term `b_n x^(n-u)` of (4)
on the two banks and the joining small arc before sending its radius
to zero. The arc cancels exactly the divergent powers from n=-2,-1.
There is no constant logarithmic term because u is strictly between
zero and one. The remaining finite part is (5). Equivalently, on the
normalization put `t-alpha=s^(N/d)`, `d=gcd(N,j)`. A possible local
residue would require `(n+1)N=j` for an integer n, which cannot hold
for 1<=j<N. These endpoint poles are of second kind; they do not supply
an independently choosable residue cycle. This proves (3) entry by
entry, with the same marked endpoint continuation as the original
small circle.

## 3. At most two derivatives give a convergent flow integral

Let p in {0,1,2} be the pole order in (4), and put

    H_j(x)=x^p f_j(x).

This is analytic at zero. Integration by parts with the endpoint
finite parts retained gives, for p>=1,

    FP integral_0^infinity x^(-u-p) H_j(x) dx
       =1/[u(u+1)...(u+p-1)]
                         integral_0^infinity x^-u H_j^(p)(x) dx. (6)

For p=0 use the original integral. Each derivative in the integration
by parts removes one negative integer power. Its factor is positive
`1/(u+p-1)` at the first step and so on. The possible finite boundary
term at zero is absent because all the exponents are nonintegral;
the divergent terms are exactly those subtracted in (5).

At infinity, `g_j(1+x)=O(x^(-(N-1)/2+u))`, so
`H_j=O(x^(p-1-(N-1)/2+u))`. Every intermediate boundary term tends
to zero. The final integrand in (6) is integrable both at zero and
infinity. Rationality and the finite product expression also give
these derivative estimates directly. Equation (6) is particularly
convenient for computing the marked period without subtracting two
numerically divergent endpoint quantities.

These derivatives act on the COMPLETE H_j, including the cyclic
resolvents, power characters and source entries. Applying them only
to the dilogarithm factor would change the original period. Neither
H_j^(p) nor the subtraction terms need be positive.

## 4. The extra terms survive an original crossing cap

The actual two-head calculation at N=2, M=1, Q=-1, x=i uses the
opposite-root u transfer with a=i, the original fusion C, D=I and
the original averaged cap with pivots (-i,i). After those contractions
the unsplit transfer and the sum of its two cyclic cross terms are
respectively

    B_nil(t)=2i/t^2,
    B_cross(t)=-2i(t^2-1)/[t^2(t^2+1)^2].         (7)

Here `A_epsilon(t)=(1+t)^(-1/2)` for either orientation. Their original
small-circle periods are both -i. However B_cross has unramified
double poles at beta=+i,-i, off the negative real dilogarithm cut.
Its coefficients there are

    at +i: b_(-2)=i, b_(-1)=-2,
    at -i: b_(-2)=i, b_(-1)= 2.

Consequently the residue sum which MUST be subtracted in (3) is

    i A_epsilon'(+i)-2 A_epsilon(+i)
      +i A_epsilon'(-i)+2 A_epsilon(-i),          (8)

and is nonzero. Thus even a whole original cap does not delete the
new cyclic-pole correction. The original crossing's external common
Cartan line multiplies both representations equally and is unchanged.

## 5. Tensoring the prescription preserves the entire source

Apply (3) to each Euler variable of the exact cyclic sewing network,
and use the ordinary original Hankel rule on its factorial variables.
Each variable has at most two cyclic-resolvent factors, irrespective
of level or braid length. The subtraction order is therefore at most
two PER EULER VARIABLE. The number of variables and of cross-sewing
types depends on the fixed word; the number of root-labelled cuts and
unramified cyclic poles still grows with N.

All pole loci in a variable depend only on its own coordinate and
the retained meridian, not on the other integration variables. The
ordered matrix contraction is finite. Its products of endpoint
Laurent expansions have independent variables; taking their finite
constant parts and ordinary residues commutes. Equivalently apply
the proved one-variable identity repeatedly to the original compact
product circles, where every integral is initially convergent.
This defines a tensor prescription even when an unregularized
multiple radial integral would fail to be absolutely convergent.

The outcome is an exact selected cyclic period with explicit endpoint
jets and pole residues, not a bare cyclic state. It retains the full
original boundary source and every peripheral factor. The required
future geometric comparison must carry this specified relative cycle.
The finite subtraction order makes that target more concrete, but
does not identify its leading hyperbolic component or prove that it
survives the final sum.

[Independent numerical contour diagnostics](../experiments/audit_cyclic_sewing_regularized_cut_cycle.py).
