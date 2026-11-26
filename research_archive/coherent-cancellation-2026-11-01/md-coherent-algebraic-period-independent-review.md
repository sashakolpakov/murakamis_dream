# Bounded independent review of the algebraic-period obstruction

1 November 2026. Read-only mathematical review. The root-authored private
note was read in full. Its Fraction checker was read in full and executed
independently with python3; every assertion passed and the process exited
zero. No public file was changed. This report does not certify any actual
knot source or hyperbolic representation.

## Verdict

No mathematical defect was found in the stated abstract counterexample.
It disproves the implication from the listed pressure/measure/algebraic
and scalar-budget properties to the desired negative-axis comparison.
It does not disprove a theorem using original triangle incidence, common
coefficient demands, or a marked geometric representation.

One exposition clarification was sent to the author: make the elimination
of the square-root coordinate explicit, as in section 3 below. The author
integrated that displayed polynomial and product into section 2; I then
read the integrated paragraph directly. The input hash recorded below is
the resulting 73940ac0 version. This is a short completion of the written
elimination step, not a failure of the algebraicity claim.

## 1. Branches, probability measure and pressure

On the slit plane the principal square root has positive real part.
The continued arctangent has no singularity in its image; its singular
points occur only at the boundary values corresponding to w=-a.
Direct differentiation gives w f_a'(w)=m_a(w), with f_a(1)=0.

On the upper negative axis, setting t=sqrt(r/a), the imaginary part is
\[
 \operatorname{Im}m_a(-r+i0)
   =\pi^{-1}\log|(1+t)/(1-t)| .
\]
This gives the stated positive density
\[
 \rho_a(r)=(\pi^2r)^{-1}
       \log|(\sqrt a+\sqrt r)/(\sqrt a-\sqrt r)|.
\]
The small-circle O(|w|^{-1/2}) and large-circle O(1/|w|) estimates for
m_a(w)/w make the keyhole Cauchy argument valid. The indentation at -a
has length times a logarithmic singularity and vanishes. The resulting
Stieltjes representation and monotone convergence give mass one.
Its endpoint orders are r^{-1/2} and r^{-3/2}; both logarithmic moments
are finite. Hence integration of the derivative, normalized at w=1,
gives exactly the logarithmic pressure of a probability measure on (0,1).

For the stated mixture the measure is atom-free, and
\(m(0+)=0,m(+\infty)=1\). Its Stieltjes representation has positive
imaginary part in the upper half-plane, so the chosen algebraic phase
satisfies \(0<|B|<1\). No negative-axis branch is reset.

## 2. Exact negative-axis loss and restoration deficit

The continued dilogarithmic integral satisfies
\[
 \operatorname{Re}\operatorname{Ti}_2(it+0)
       =(\pi/2)\log_+t.
\]
Equivalently, the real logarithmic derivative of f_a on the upper
negative axis is zero for r<a and one for r>a. Its value at zero and
continuity at r=a supply the stated absolute constant.

For L=log256 and C=(4/pi)Ti_2(1/16), the normalized negative-axis
objective is exactly
\[
 (s+L)_+/3+2(s-L)_+/3-s_+-L/3-C,\qquad s=\log r.
\]
Its successive slopes 0,1/3,-2/3,0 prove that its maximum is -C.
Thus chi=C<2/25.

The restoration function has strictly positive second derivative.
Its first derivative tends to -1 and 1/2 at the two ends, so there is
one finite minimizer. I independently differentiated the t=e^{z/2}
formula to obtain
\[
 V'(2\log t)=-1/6+
 [4\arctan(t/16)-2\arctan(1/(16t))-3\arctan(1/t)]/(3\pi).
\]
The exact checker encloses V(2log8), its derivative, and the positive
derivative at 2log9 in the intervals stated in the note. The minimizer
therefore lies between these arguments. The tangent bound at 2log8,
using 2log(9/8)<1/4, gives -min V<.28; evaluating there gives
-min V>.27. Thus D-chi>.19, with no numerical extrapolation.

The checker uses genuine rational interval operations, alternating
remainders for arctan and Ti_2 on (0,1), and a positive geometric
remainder for logarithms. The decimal conversions occur only in output.

## 3. Algebraic phase and selected critical point

The exact cubic relation is correct. An explicit rational eliminant is
obtained by putting
\[
 P(t,B)=B^3(1-16it)^2(16-it)^4
           -(1+16it)^2(16+it)^4.
\]
The product P(t,B)P(-t,B) is even in t and has rational coefficients.
Substitution t^2=w is consequently an actual polynomial in w,B.
Its leading B^6 coefficient is
\[
 (1+256w)^2(256+w)^4,
\]
so it is not identically zero. On the positive axis the selected
square-root and cubic branches are regular.

The critical equation B(w)(1+i sqrt(w))/(1-i sqrt(w))=1 has the
specified logarithmic lift: m(w)+atan(sqrt(w))/pi is strictly between
0 and 3/2, so its only possible integer is one. Strict positive
derivative selects exactly one positive solution. Substitution in
the displayed algebraic equations gives an algebraic w_*; the relevant
equation is not identically zero, as its positive branch is strictly
monotone. The period formula includes the essential constant q(0).

## 4. Effective response and scalar geometric-budget test

The mean and response are exactly
\[
 \nu=1/3+(2/(3\pi))\arctan(1/16),\qquad
 \kappa=16/(257\pi).
\]
The response is positive and obeys the probability-measure variance
bound kappa<=nu(1-nu). The logarithmic derivative of each component
response lies between -1/2 and 1/2, so its positive mixture has the
claimed two-sided response comparison for every real z,s.

The rational lower bound for alpha is correctly directed:
using delta=(2/3)atan(1/16)<1/24,
\[
 \cos(\pi\nu)>1/2-1/2304-7/192.
\]
Multiplication by 7/5 and the alternating upper bound for sin(.7)
give alpha>.7. On [0,.7], cos t>.75 and asinh(.75)=log2>2/3.
Together with pi<22/7, this proves
\[
 W(\nu)/\pi>49/165>.29>D+.01 .
\]
Hence a positive budget slack g=pi/50 is indeed allowed. This is only
the same scalar form of the known geometric budget; it does not supply
the original group representation that proved that budget for sources.

## 5. Stable finite approximations and their precise limit

Rational empirical points in (0,1) approximating the constructed
probability measure give homogeneous real-stable binary products with
positive coefficients and P_d(1,1)=1. On every compact subset of the
slit plane, log(1-p+pw) and all fixed w-derivatives are jointly
continuous and bounded for p in [0,1]. Weak convergence and a finite
net thus give locally uniform convergence of d^{-1}log P_d(w,1),
and of the fixed derivatives, to the stated pressure.

This supplies the abstract stable realization and all fixed local
pressure jets. It does not give a pointwise negative-axis limit at
every polynomial zero, nor an original q-Hahn determinant, sphere
source or face-coefficient realization. The draft explicitly retains
these limits. The computed continuous negative-axis supremum suffices
for the abstract failed implication.

## 6. Hashes of the reviewed inputs

- /private/tmp/md-coherent-algebraic-period-obstruction.md: 73940ac0a1e994547f5196f5b7241f9f0f0f09e6015048aedef9dfaf6876ec81
- /private/tmp/md-coherent-algebraic-period-check.py: 681db266a45f03b4d9abb1f6878438fbe149b89f8ca9c6764105f593febc3901
- /private/tmp/murakamis_dream-publication/notes/research_cap_algebraic_boundary_curve_and_volume_period.md: ea3ca648522d1c720e2f7f7d45a9e9f92fc7ca95b4ef157be28b57050da4cd82
- /private/tmp/murakamis_dream-publication/notes/research_cap_root_measure_from_classical_pressure.md: ec8af7e480c81845b99ae923d9dd60f2be353b80b7b6a42ea4521b5d0ebed5d8
- /private/tmp/murakamis_dream-publication/notes/research_global_cap_effective_response_criterion.md: 14bbf99f1422b4d11d969c65919132824680be1a33bba6875c0e757d3b206754
- /private/tmp/murakamis_dream-publication/notes/research_one_cap_original_chain_volume_budget.md: 461dcd9ef98cae11211523421a6da983fb99dd0365375b3ea96f8de7dd15a91b
