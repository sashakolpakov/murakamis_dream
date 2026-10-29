# The finite cover and the dilogarithm period are parts of one local object

Research note, 25 October 2026. This reconstructs the b^2=1/n case of
Garoufalidis--Kashaev,
[Evaluation of state integrals at rational points](https://arxiv.org/abs/1411.6062),
Theorem 1.9. The formula is standard; its proof is supplied here to fix
the object and its normalization without adopting that theorem as a premise.
It explains which data a proposed algebraic torsor must retain in comparing
the finite cyclic construction with the Faddeev state already used here.

## 1. An exact identity, for every positive integer n

Set b=1/sqrt(n), c_b=i(b+b^(-1))/2, omega=exp(2pi i/n), and

    F_n(z)=Phi_b(z/(2pi sqrt(n))-c_b),
    D_n(X)=product_(j=1)^(n-1)(1-omega^j X)^(j/n).

Initially take Re z<0 and 0<Im z<2pi(n+1). Define all logarithms by
their convergent series in exp(z/n), with D_n(0)=1. Then exactly

    F_n(z)= exp[i Li_2(exp z)/(2pi n)]
                  (1-exp z)^(1+i z/(2pi n)) / D_n(exp(z/n)). (1.1)

The formula extends by continuation with its recorded branches. The
left side is meromorphic in z; arbitrary independent branch choices
on the right do not give that same meromorphic function.

## 2. Independent residue proof

Start from the independently audited defining integral for Phi. Substitute
its integration variable w=sqrt(n)*t. The exponential shift by -c_b
cancels the corresponding factors in the two hyperbolic sines, giving

    log F_n(z)=integral_(R+i0)
           exp(-i z t/pi)/[(exp(2t)-1)(exp(2nt)-1)] dt/t.

The stated imaginary strip gives exponential tails. A horizontal line at
any height delta with 0<delta<pi/n represents the same integral.
Differentiation gives

    d_z log F_n(z)=(-i/pi) integral_(R+i delta)
                    exp(-i z t/pi)/[(exp(2t)-1)(exp(2nt)-1)] dt. (2.1)

Close upward when Re z<0. Rectangles of height pi(k+1/2)/n stay away
from both pole lattices. Their top sides decrease exponentially in
height, and the vertical sides disappear by the same strip estimates.
Thus the residue sum converges absolutely. At t=pi i k/n with n not
dividing k its residue is

    exp(k z/n)/[2n(omega^k-1)].

At the double pole t=pi i l, l>=1, expand the denominator to first
order beyond its quadratic zero. Its residue is

    exp(l z)/(4n)*[-i z/pi-(n+1)].

The prefactor in (2.1) multiplies these residues by two. Consequently

    d_z log F_n(z)
      =sum_(k>=1,n not dividing k) exp(k z/n)/[n(omega^k-1)]
          -sum_(l>=1) exp(l z)*[(n+1)/(2n)+i z/(2pi n)]. (2.2)

On the other hand

    sum_(j=1)^(n-1) j omega^(jk)
      = n/(omega^k-1)        if n does not divide k,
      = n(n-1)/2             otherwise.

Expanding the logarithmic derivative of the right side of (1.1)
therefore gives precisely (2.2). Both sides tend to one at the left
end of this strip, by the defining Phi estimate and the convergent
series. Their ratio is constant in z and equals one. This proves
the full identity and its scalar normalization, uniformly in n.

No semiclassical limit is used in this evaluation. The contour estimates
justify a residue calculation at one fixed n, rather than comparing
unproved recurrences with an unspecified periodic factor.

## 3. Why the finite Kummer cover alone is insufficient

The exact shift identities are

    F_n(z+2pi i)=F_n(z)/(1-exp(z/n)),
    F_n(z+2pi i n)=F_n(z)/(1-exp z).                     (3.1)

Thus the n-step transport is not the identity. A finite cyclic function
is obtained only after removing this norm transport. Put u=exp z,
X=exp(z/n), and choose h^n=1-u. Then

    D_n(omega X)/D_n(X)=(1-X)/h

on the normalized lift. Its inverse has norm-one transport h/(1-X).
This is the Hilbert 90 part. The remaining factor in (1.1) carries
the noncyclic central transport (1-u)^(-1/n).

At rational b the two original quantum shifts are commensurate. Their
functional equations alone therefore leave arbitrary central periodic
functions of u. A norm-one argument cannot fix that factor. Formula
(1.1), obtained from the defining integral and its normalization, fixes
it explicitly.

## 4. The continuous Heisenberg period

On the universal cover of u in P^1 minus {0,1,infinity}, define

    z=Log u, w=Log(1-u), S=Li_2(u)+z w.

They solve the triangular system

    dz=du/u, dw=-du/(1-u), dS=z dw.                     (4.1)

Any two solutions on a simply connected domain differ uniquely by

    (z,w,S) -> (z+a,w+b,S+a w+c),

where a,b,c are constants. To prove this, subtract the first two
equations, obtaining constants a,b; subtract dS and then a dw,
obtaining the remaining constant c. Their composition is the
Heisenberg group law, with its central cross term. A basepoint value
fixes the horizontal section uniquely.

The exact local quantum function is now

    F_n(z)=exp[w+i S/(2pi n)] / D_n(exp(z/n)).            (4.2)

It combines the continuous dilogarithm period with the finite algebraic
root data. This is the reason to seek a Heisenberg/dilogarithm torsor
with connection, not just a scalar G_m-torsor.

For odd n this can be written directly in the determinant-normalized
coordinates of `heisenberg_period_torsor.md`. With h=(n-1)/2 choose

    x=exp(z/n), c=exp(w/n), s=D_n(x)/c^h.

Then s^n is exactly the centered product (2.1) of that note. Thus
the local identity becomes the single period evaluation

    F_n(z)=s^(-1)
           exp[(n+1)w/(2n)+i S/(2pi n)].               (4.3)

The algebraic coordinate s and the horizontal period coordinates
(z,w,S) live on the compatible finite/continuous Heisenberg covers.
Under z -> z+2pi i, s changes by (1-x)/c and S changes by 2pi i w;
their multipliers combine to 1/(1-x), exactly (3.1). This checks
the monodromy and the full scalar, not just its logarithmic derivative.
Equation (4.3) is an exact local realization of the proposed
period-torsor viewpoint.

Writing R(u)=Li_2(u)+(1/2)Log u Log(1-u), its connection is the
symmetric form

    dR=(1/2)(z dw-w dz).

This is the primitive of the logarithmic symplectic form used in
face/edge reduction. It is the classical period structure underlying
the same gluing problem. Branch constants and flattenings are part
of that structure.

Algebraic triviality of an underlying unipotent torsor does not imply
a rational horizontal section. Already dz=du/u has none over C(u):
the derivative of a rational function has zero residue at every point,
whereas du/u has residue one at zero. Hilbert 90 and rigidity of the
*flat* period object address different statements; the connection must
remain in the comparison.

## 5. The global obligation is now identifiable

For any finite product of local Phi factors and a rational Gaussian,
(1.1) is an exact factorization of the integrand at b^2=1/n into
cyclic algebraic functions and dilogarithm periods on a specified
logarithmic cover. This applies uniformly to the state-integral class
in the existing notes. It does not by itself evaluate the remaining
multidimensional integral or identify its selected cycle with a finite
contraction.

In the existing state conventions b^2=1/n means exactly
h=b^2/(1+b^2)^2=n/(n+1)^2. A global comparison must retain this h,
the Q_b spectral rescaling, its Jacobian and the peripheral variables.
Replacing h by 1/n before matching states would lose finite-level data.

### 5.1 The exact central character on the semiclassical state

There is a second parameter distinction. In the actual state the
local argument is Z=y/(2pi sqrt(h)). At b^2=1/n,

    Z=(n+1)y/(2pi sqrt(n)),
    X=-exp(-pi i/n) exp((n+1)y/n),
    X^n=exp((n+1)y)  for odd n.                         (5.1)

To apply (1.1) to this argument, substitute exactly

    z_n=(n+1)(y+pi i).

Then z_n/(2pi sqrt(n))-c_b=Z, exp(z_n)=exp((n+1)y), and

    exp(z_n/n)=omega X.                                (5.2)

The root-of-unity deck shift in (5.2) must also be retained. For Re y<0,
-pi<Im y<pi this substitution lies in the initial domain of the exact
identity, and elsewhere one uses matched continuation.

Consequently a fixed semiclassical shape coordinate y does not follow
a fixed central character t on the finite splitting covers: it follows
t_n=exp((n+1)y). A size bound for a normalization unit at fixed central
t cannot automatically be used along this sequence. The proposed
global period comparison must specify this map of parameters, its deck
lift, and the selected integration cycle. This is an exact substitution
in the state definition, not an asymptotic assertion or a disproof of a
possible comparison with fixed-character cyclic invariants.

The desired intrinsic period object must preserve the connection,
the determinant roots, the peripheral lifts, and the period class.
A global identification of that object would make comparisons between
triangulations a descent problem. The volume assertion would then be
one compatibility statement with its classical regulator, rather than
a new proof for every knot. That global identification and comparison
remain unproved; the exact local identity is a bridge toward them.

`rational_period_pushforward.md` now applies this identity to the full
rational Gaussian--Faddeev integrand class. Its exact folded period
retains the scaled source contour and all generic peripheral factors.
It identifies the finite translation Koszul complex and local gluing
residues, proves a source-pole cancellation criterion, and retains
regular specialization when a gluing point reaches a polar divisor.
The global cycle localization and cross-level norm comparison are
still separate obligations.
