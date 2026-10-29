# An exact factorial interpolation for the original selected contours

28 October 2026. The original finite quantum factorials admit an explicit
holomorphic interpolation with a uniform complex dilogarithm expansion.
This permits a contour representation of the ACTUAL finite state sum
without replacing a finite Euler polynomial by its wrong exterior
branch. The lattice values, reflection phase and original support cycle
are all retained. A contour carrying a nonzero geometric saddle is still
required; the interpolation does not select that saddle by itself.

This is within the existing Barnes/double-sine analytic-difference
framework, not a novelty claim for a special function. For coverage see
[Ruijsenaars, On Barnes' Multiple Zeta and Gamma Functions](https://ir.cwi.nl/pub/2100)
and [Narukawa, multiple sine functions and elliptic gamma functions](https://arxiv.org/abs/math/0306164).
Only coverage is used from those papers. The product, normalization,
functional identities and asymptotic comparison needed here are proved
below directly. They concern the ORIGINAL root factorial, not a newly
normalized knot state.

## 1. A convergent whole function with the exact lattice values

Fix an integer N>=2, Q=exp(2 pi i/N). On the strip -1<Re z<N define

    G_N(z)=(2 pi/N)^z Gamma(z+1)
       * product_(k>=1)
          Gamma(Nk+z+1)/[Gamma(Nk-z)(Nk)^(2z+1)].       (1)

All positive-base powers use the real logarithm. Each Gamma argument
has positive real part in this strip. On every compact z set the
logarithm of the kth factor is O_(N,K)(k^-2): in the Gamma-ratio
expansion the 1/k term cancels. More explicitly, its leading term is

    -z(z+1)(2z+1)/(6N^2 k^2).

The product and its logarithmic derivatives therefore converge locally
uniformly. It is holomorphic and nonzero on the strip and G_N(0)=1.
Gamma's functional equation gives on overlapping strips

    G_N(z+1)/G_N(z)
       =(2 pi/N)(z+1)
           product_(k>=1)[1-(z+1)^2/(N^2 k^2)]
       =2 sin(pi(z+1)/N).                            (2)

The last equality is the ordinary convergent sine product. This also
gives the meromorphic continuation of (1). Define the marked factorial

    Fhat_N(z)=exp[i pi z(z+1)/(2N)-i pi z/2] G_N(z).  (3)

Then EXACTLY

    Fhat_N(z+1)=[1-Q^(z+1)] Fhat_N(z),
    Fhat_N(0)=1,
    Fhat_N(n)=(Q;Q)_n, 0<=n<N,                     (4)

where Q^z always means exp(2 pi i z/N). In particular the interpolation
is attached to the original finite state before any asymptotic choice.

For any marked alpha and nonnegative integer n where the ratio is
regular, (4) also gives

    Fhat_N(alpha+n)/Fhat_N(alpha)=(Q^(alpha+1);Q)_n. (5)

Thus color-shifted factorials have the same exact interpolation. Their
whole meridian marks and original prefactors remain part of the state.
This is a fixed-root identity, not a moving-q normal-jet theorem.

## 2. Reflection is exact, with no undetermined periodic factor

The whole sine product satisfies

    G_N(z)G_N(N-1-z)=N.                            (6)

Here is a proof that fixes a possible periodic ambiguity. Differentiate
the logarithm of the left side using (1), initially on the stated strip.
Writing psi for the logarithmic derivative of Gamma, the partial sum
through k=K telescopes to

    psi(NK+z+1)-psi(N(K+1)-z).

It tends to zero locally uniformly as K tends to infinity. Hence the
left side is constant. At z=0 its value is the literal product
product_(j=1)^(N-1)2sin(pi j/N)=N, obtained by evaluating the derivative
of t^N-1 at t=1. This proves (6). The corresponding marked identity is

    Fhat_N(z)Fhat_N(N-1-z)
       =N exp[i pi z(z-N+1)/N].                    (7)

The phase in (7) cannot be discarded in a complex contour deformation.

## 3. A finite Barnes-G formula for independent computation

Let B denote the Barnes G function with B(1)=1 and
B(w+1)=Gamma(w)B(w), normalized by its convergent Weierstrass product.
The infinite product (1) equals the finite expression

    G_N(z)=(2 pi/N)^z Gamma(z+1)
       * product_(r=0)^(N-1)
          B(1+(r-z)/N)/B(1+(r+z+1)/N).             (8)

For completeness its scalar is fixed, not inferred from a recurrence.
Apply Gamma multiplication to each factor of (1), and put

    a_r=(r+z+1)/N, b_r=(r-z)/N.

The product through k=K becomes the right side of (8) times

    H_K=Gamma(K+1)^(-(2z+1))
             product_r B(K+1+a_r)/B(K+1+b_r).

One has H_K(0)=1 by telescoping in r. Direct differentiation of the
defining Weierstrass product gives

    d/dw log B(1+w)=w psi(1+w)-w-1/2+(1/2)log(2 pi).

The ordinary uniform digamma expansion on a positive large argument
therefore gives partial_z log H_K=O_Kcompact(1/K), since
sum_r(a_r+b_r)=N. Integrating from zero to z proves H_K->1.
This establishes (8) with scalar one; it does not require a quoted
multiple-Gamma normalization theorem.

## 4. Uniform complex asymptotics, including the first correction

Let K be any compact subset of 0<Re x<1. Define the analytic primitive

    J(x)=integral_0^x Log(2sin(pi t)) dt,

continued from 0<x<1, with its integrable logarithmic endpoint at zero.
The sine has positive real part on this strip, so its indicated
logarithm is single-valued there. Uniformly on K,

    log G_N(Nx)
       =N J(x)+(1/2)Log(2N sin(pi x))
                   +pi cot(pi x)/(12N)+O_K(N^-3).     (9)

The logarithm and square-root marks are the ones positive on the real
interval. Every fixed derivative also satisfies the corresponding
uniform remainder bound on a smaller compact set.

### Direct proof with a summable remainder

Use the elementary Gamma Stirling expansion through 1/(12w), with
remainder O(|w|^-3) in a closed right-half-plane sector. That remainder
bound follows, for example, by integrating the bounded periodic
fourth Bernoulli polynomial in the Euler summation remainder; its
integral is bounded by a constant times integral_0^infinity|w+t|^-4 dt.
For x in K all arguments Nx and N(k+x),N(k-x) remain in such a sector,
uniformly in k. The kth logarithmic factor in (1) becomes

    N phi_k(x)+(1/2)Log(1-x^2/k^2)
       +(1/(12N))[1/(k+x)-1/(k-x)]
       +O_K(N^-3 k^-3),

where

    phi_k(x)=(k+x)Log(1+x/k)-(k-x)Log(1-x/k)-2x.

The remainders are summable. Since phi_k(0)=0 and
phi_k'(x)=Log(1-x^2/k^2), the sine product sums the leading terms
to J(x) after including the Gamma(Nx+1) factor. It likewise sums
the half-logarithms to (1/2)Log(2N sin(pi x)). Finally

    1/x+sum_(k>=1)[1/(k+x)-1/(k-x)]=pi cot(pi x)

gives the displayed 1/N term. This proves (9) with the stated
uniform remainder. Cauchy's formula proves the derivative assertion.

Equivalently, writing X=exp(2 pi i x) on the same logarithmic strip,

    Fhat_N(Nx)=sqrt(iN(1-X))
        *exp{N[Li_2(1)-Li_2(X)]/(2 pi i)
                       +pi cot(pi x)/(12N)+O_K(N^-3)}. (10)

The square root means sqrt(2N sin(pi x))exp(i pi x/2), not an
independent principal-root reset. The equality of the leading
primitives follows by differentiating and fixing the value at x=0.
No continuation through an unrecorded dilogarithm cut occurs in
0<Re x<1, since X avoids the real interval [1,infinity).

Unlike a pointwise assertion about a finite Euler polynomial, (10)
holds on full complex compact subsets of this strip. In particular
it remains useful when a geometric coefficient saddle has a
nonzero imaginary index coordinate.

## 5. The original finite sum has a marked residue cycle

Take the ACTUAL finite coefficient sum for a fixed braid, after its
integral closure equations have been solved as in the existing
normal-period calculation. Its dimension d depends on the word,
not on N. Write its allowed lattice support as S_N. All factorial
arguments at an allowed point are integers between zero and N-1;
retain every Gaussian, pivot, cap, framing and peripheral factor.

Replace each factorial in that same summand by Fhat_N of its
original affine index form, using (5) for a marked color shift.
Call this meromorphic interpolated summand I_N(z). It agrees with
the literal original coefficient at every allowed integer point.
Choose small positively oriented product circles about the points
of S_N, with no other integer poles or interpolation poles inside,
and let Gamma_N be their oriented sum. Then exactly

    sum_(k in S_N) I_N(k)
      =(1/(2 pi i)^d) integral_(Gamma_N)
                 I_N(z) product_(j=1)^d [pi cot(pi z_j) dz_j]. (11)

Each cotangent has residue one. Equation (11) is therefore a direct
multivariable residue identity, with the original finite support
encoded in its specified cycle. It does not replace that cycle by
a preferred infinite contour or omit a finite-head wall.

At completeness, on any complex tube where every scaled factorial
argument has real part strictly between zero and one, the interpolated
summand has no factorial zero or pole. Formula (10) gives its actual
complex phase and a uniform nonzero leading amplitude there. The
cotangent pole lattice and the support boundary still have to pass
through any proposed deformation of Gamma_N. Neither a nonzero
interpolant nor a unique critical point establishes its intersection
coefficient with the original cycle.

This makes a possible route to the main theorem more concrete: a
source-preserving deformation of (11) to a positive geometric chain
could use a uniform complex expansion of the SAME lattice summand.
The whole contour and boundary estimate, including noncancellation,
remain necessary. In particular no 5_2 or broad knot volume theorem
is asserted by this interpolation result.

[Exact functional-equation and complex-asymptotic diagnostics](../experiments/audit_exact_factorial_interpolation.py).
