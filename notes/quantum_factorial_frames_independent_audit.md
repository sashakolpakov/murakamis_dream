# Independent audit of the actual quantum-factorial frames

Audit, 27 October 2026.
[quantum_factorial_frames_and_cyclotomic_source.md](quantum_factorial_frames_and_cyclotomic_source.md)
passes the uniform frame-period, marked primitive, conditioning and
eigenflag-current checks. The exact balanced-source comparison in
[integral_color_global_q_difference_source.md](integral_color_global_q_difference_source.md)
also checks.

## 1. Exact frame orientation and actual source

The basis identity \(p_j=R_jf_j\) implies
\(A_p=R^{-1}A_fR\); the printed coupon transformation has that
orientation. The positive factors are the exact ratios of
q-falling to ordinary falling factorials.

The regular balanced basis multiplier of the global q-difference note
is the inverse of the coordinate-conjugation multiplier in
[the source detour audit](integral_color_source_detour_audit.md).
Indeed
\[
 {n\choose j}_{\rm sym}=q^{-j(n-j)}{n\brack j}_{Q}
\]
identifies the two formulas exactly, including endpoint phases.
The source column, dual row and cup/cap transformations in the
regular basis all follow with their printed inverse factors.

The normalization distinction is substantive and is explicit in
the global-source note. The symmetric Gauss pair is
\((\rho E_q,\rho F_q)\). Relative to the original balanced convention
\((\rho^2E,F)\), this is a common Hopf rescaling, or equivalently
the indicated weight-dependent change of integral lattice.
Its \(E\otimes F\) factor cancels in the universal crossing; its
Cartan and diagonal pivot stay unchanged. The ordinary integral
generators and the literal balanced generators need not both
have the same regular \(q=1\) lattice. This distinction cannot
be omitted from a comparison of source jets.

The reciprocal polynomial chart \(J_n\) gives the stated global
q-difference formulas. A particular old balanced Weyl map, if
used, must additionally be conjugated by its actual diagonal
frame. It need not equal the bare reciprocal matrix in the new
coordinates.

## 2. Uniform scalar frame period and its marked primitive

The Riemann-sum estimate is uniform, including the resonant endpoint.
Writing
\[
 \log b_\lambda(x)=\log(1-\lambda x)+g(\lambda x)
\]
leaves a \(C^1\) function \(g\) on the whole closed interval.
Its normalized sum error is \(O(1/N)\).
Monotonicity controls the logarithmic sum away from its last
interval by \(O(\log N/N)\); the final interval has integral
bounded by \(O((1+\log N)/N)\), uniformly even as \(\lambda\to1\).
The denominator \(b_\lambda(1/N)\) contributes only \(O(N^{-2})\)
to the normalized logarithm. This proves the claimed estimate.

Direct differentiation of the marked dilogarithm expression gives
\[
 B_s'(x)
  =sx/2+\log(1-e^{-sx})-\log(sx)
  =\log\!\left(\frac{2\sinh(sx/2)}{sx}\right).
\]
With the common continuation mark this is real on the specified
imaginary-\(s\) path. At \(s=0\) the common additive singular
constant in \(B_s\) cancels in its difference; the period tends
to zero. No unmarked dilogarithm constant is being discarded.

The endpoint sine product gives precisely
\[
 R_n=\frac{N}{(2\sin(\pi/N))^{N-1}(N-1)!}.
\]
All factors satisfy \(0<[k]_q/k\le1\), so the condition number is
\(R_n^{-1}\). The limit \(\log(2\pi)-1\) follows with the printed
sign. This conditioning is the same in a common diagonal metric.

## 3. Canonical shears and the two negative inverse-flag bubbles

The scalar products of the principal symbols give the stated
Casimir. Solving their two eigenline equations gives exactly
the printed plus and inverse flag factors.
The plus shear fixes \(T=va\), preserves \(dv\wedge da\), and
on the real sphere only changes its angle. Its generating
function in the stated primitive \(\log v\,dT\) has derivative
\(s(1-T)/2\), as claimed.
For the Chern primitive \(-a\,dv\), the corresponding primitive
difference instead is \(d(sT^2/4)\); these conventions are
compatible through the exact change of primitive.

The p-to-f principal shear has logarithmic shift
\(-\log J_s(1-T)=-S_\lambda'(T)\), matching the actual
factorial-period sign. Its nonuniform endpoint explains why
the old p-frame plus bubble is not an invariant obstruction.

For the inverse flag, the latitude lies in \([0,1]\), tends to
\(T\) in the interior, and has endpoint values \(1,0\) below
resonance. Integration by parts against the angularly averaged
test function gives the weak limit
\(\omega_\Gamma-\delta_{T=0}-\delta_{T=1}\).
The local maps are \(-1/\bar\zeta\) and \(\bar\zeta\), each
of degree \(-1\), fixing both signs independently.

## 4. Scope of the valid interpolation

The exact ordinary integral-color closure uses \(K\) and its
ordinary twist. The frozen root closure has its different
whole-clock adapter, explicitly retained in both notes.
The root pivot is not an off-root pivotal element merely
because the module quotient exists.

The smooth principal shear alone does not identify its literal
pullback with finite star transport. A specified diagonal matrix
conjugation does give an exact inner star automorphism, with its
source transformed too; it does not construct a global geometric
A-branch. Exponential frame conditioning,
actual inverse-eigenflag marking, endpoint currents and source
coupons remain. The nearby-principal-root resonances of the
actual scalar color further prohibit a uniformly nonvanishing
positive WKB approximation along the whole real path.

## 5. The exact finite unitary shear

The added diagonal shear is also correct. Put
\[
 U_j=q^{Nj-j(j+1)/2},\qquad
 \widehat a=J_-/n,\quad\widehat b=J_+/n,\quad
 \widehat T=J/n.
\]
The two adjacent ratios are \(q^{j-N}\) and \(q^{N-j-1}\).
Binomial summation therefore gives exactly
\[
 \sigma_{U\widehat aU^{-1}}
     =m^{-1}q\,a[1+(q-1)T]^{n-1},\qquad
 \sigma_{U\widehat bU^{-1}}
     =mq^{-1}\,b[1+(q^{-1}-1)T]^{n-1},
\]
and \(\widehat T\) is fixed. Here \(a=z/(1+vz)\) and
\(b=v/(1+vz)\) are the two normalized off-diagonal coordinates.
Their principal limits are \(a/r,rb\), with
\(r=e^{s(1-T)/2}\), giving precisely the source shear.

For real \(\lambda\), every \(U_j\) has modulus one. This makes
conjugation unitary in any common diagonal coherent metric and
leaves the diagonal pivots unchanged. It is an exact automorphism
of the finite symbol algebra with its star product; only its
principal limit is the literal pullback by the smooth source map.
Sources and inserted matrices still transform by that same
conjugation.

For the regular balanced basis multiplier,
\[
 D_{{\rm basis},j}U_j
      =\frac{M^j}{{n\choose j}_{\rm sym}},
 \qquad M=-q^N.
\]
At the root this is one, so \(U=D_{\rm basis}^{-1}\).
Off the root its residual q-binomial gauge remains; it is not
a uniformly bounded scalar normalization.
Finally
\[
 U_n=q^{N(N-1)/2}\big|_{q=q_N}
       =i^{N-1}=i^{N+3}=\epsilon_N.
\]
This exact endpoint phase uses the marked path. It does not
permit dropping the other pivotal, ribbon or source characters.
