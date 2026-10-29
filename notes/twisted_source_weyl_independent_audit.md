# Independent audit of the twisted source and balanced Weyl cocycle

Audit, 27 October 2026. The proof in
[twisted_cotangent_source_and_weyl_gluing.md](twisted_cotangent_source_and_weyl_gluing.md)
passes this independent sign, scalar and endpoint check. No tests
were rerun.

The cotangent transition is
\(b'=w-w^2b,\ w'=1/w\), so
\(dw'\wedge db'=dw\wedge db\) and
\(-b'dw'=-b\,dw+d\log w\).
On the compact sphere the local primitive is the \(O(1)\) Chern
connection, with curvature period \(-2\pi i\) and positive normalized
class \(-\omega_0/(2\pi i)\).
The complete finite section formulas preserve \(O(N-1)\), and its
reciprocal coordinate change gives precisely
\((K,E,F)\mapsto(K^{-1},-F,-E)\).
The half-form bundle identity and its physical curvature scale
also agree with these signs.

For the generic meridian comparison, let
\[
 d_j(M)=M^j\frac{(Q;Q)_j}{(M^2Q;Q)_j},\qquad W_M=D_MC.
\]
After reversal the raising coefficient of \(E_M\) is
\((M^2Q^{j+1}-1)/M\).
Multiplication by
\[
 \frac{d_{j+1}}{d_j}
   =\frac{M(1-Q^{j+1})}{1-M^2Q^{j+1}}
\]
gives exactly \(-(1-Q^{j+1})\).
The inverse ratio and
\(1-Q^{-j}=-Q^{-j}(1-Q^j)\) give \(-E_{M^{-1}}\)
for the other generator. The clock and both zero endpoint
coefficients match too. At the unrolled level,
\(\alpha'=2(N-1)-\alpha\) gives exactly \(H\mapsto-H'\);
this is the retained lift, not merely an equality modulo \(2N\).

The diagonal product of two Weyl matrices is
\(d_j(M^{-1})d_{N-1-j}(M)\).
Its ratio between consecutive \(j\)'s is one, so its scalar is
its \(j=0\) value:
\[
 c_N(M)=\frac{N M^{N-1}}{S_N(M^2)}.
\]
Here the two full products are
\((Q;Q)_{N-1}=N\) and
\((M^2Q;Q)_{N-1}=S_N(M^2)\), with no phase missing.
This is invariant under \(M\mapsto M^{-1}\), equals one at
completeness, and has exactly
\(N\sinh u/\sinh(Nu)\) as its whole \(M=e^u\) germ.
The marked full dimension function therefore gives the printed
\(c_N=(N/\eta_N)d_N\).

For odd levels, pairing \(Q^r,Q^{-r}\) in the norm of the
half product leaves
\(S_N(M^2)/(NM^{N-1})\). For even levels the paired product
omits \(1+M^2\), and the missing scalar is exactly
\[
 \frac{(1+iM)(1+i/M)}{(1+i)^2}
       =\frac{1+M^2}{2M}.
\]
The two printed factorial identities supply their respective
factors \(N\) and \(N/2\). Thus both rational splittings satisfy
\(\beta(M)\beta(M^{-1})=c_N(M)^{-1}\), including \(N=2\).
For even \(N=2m\), the marked \(q^m=i\) places the chosen phase
in the specified root coefficient field. Both splittings equal
one at \(M=1\), where \(D_M=I\) and the original complete
source is fixed by reversal.

The result is an explicit splitting, not a uniqueness assertion:
norm-one gauge changes can give other rational splittings.
Its zero/pole divisors and its nonconstant meridian germs remain
part of the source lattice. The note correctly retains these
data and does not infer generic coupon invariance, an arbitrary
unipotent dressing, a geometric stationary coefficient, or the
volume norm from the order-two gluing alone.
