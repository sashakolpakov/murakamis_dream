# Independent audit of pointed relative Ward localization

Audit, 27 October 2026. The proof in
[ward_source_localization.md](ward_source_localization.md) is sound
as a boundary/source homotopy statement. No crossing, coproduct,
Hopf-pivotal, or multiplicative compression is claimed or supplied.
No new matrix tests were needed.

## 1. Source normalization and the chain maps

For a nonempty retained set of size \(m\), the formulas
\(\psi_S=P\psi,\ \phi_S=(N/m)\phi P\) give
\(\phi_S\psi_S=1\). Hence \(e_S\) is rank one, idempotent,
and has trace one. The new row and the original row both
take value one on \(I_N\). Therefore their difference equals
that difference composed with \(h_N\delta_N\), exactly as
claimed. This requires the matrix Ward differential; it does
not descend to a homotopy in the color relative complex alone.

The compressed \(K\) eigenvalues are distinct. Every skip
coefficient is a product of \(1-Q^r\) with \(1\le r<N\);
it is nonzero. Thus the retained path is connected and the
split image Ward complex has kernel precisely \(kI_S\).

For
\[
 c_1=\delta_Sc_0h_N,\qquad s_1=\delta_Ns_0h_S,
\]
the identities \(c_0i_N=i_S,\ s_0i_S=i_N,\ c_0s_0=I\)
give the chain-map equations directly. In particular
\[
 c_1s_1
 =\delta_Sc_0(I-i_Np_N)s_0h_S
 =\delta_Sh_S=I
\]
on the image complex. With the stated order
\(H=(I-s_0c_0)h_N\), one gets
\[
 H\delta_N=I-s_0c_0,\qquad
 \delta_NH=I-s_1c_1.
\]
These calculations remain valid for \(m=1\), where the
retained degree-one image is zero.

## 2. The relative sign and the whole normal

For total differential
\(d_R\otimes I+(-1)^pI\otimes\delta\), \(p=\deg_R\),
the induced Ward homotopy is
\((-1)^pI\otimes H\). Its two \(d_R\) contributions cancel;
its remaining terms are \(I\otimes(\delta H+H\delta)\).
The displayed relative sign is therefore correct.

The marked root \(\alpha(U)^N=U,\ \alpha(1)=1\) exists
uniquely over \(k[[U-1]]\). Root orthogonality gives the
specified regular idempotent and
\[
 \phi_{S,U}(f)=
 \frac{\operatorname{Tr}(f)-f(\alpha)}{N-1}.
\]
For a degree-\(<N\) representative the trace is \(Nf_0\);
the carry \(f_{N-1}(A^N-U)\) is consequently retained.

There is a useful subtlety which the proof handles correctly:
localizing \(C_U\) at \(A-1\) does not literally delete the
entire marked branch over the punctured normal base. That
branch has \(\alpha-1\) invertible after \(U-1\) is inverted.
The new functional instead kills the marked summand as a
whole and extends by zero there. It is regular on the
retained summands, where \(A-1\) is a unit.

The extended \(K\)-differences and interior \(F\)-entries
are units over the formal base, so the boundary Ward
retractions extend regularly. An extra cyclic wrap does
not change the interior reconstruction on the split
image complex. This is not an internal Hopf extension.

## 3. There is an explicit obstruction to network compression

The composition defect is exactly
\[
 c_0(CD)-c_0(C)c_0(D)=LC(I-P)DJ.
\]
For retained \(i,j\) and deleted \(d\), choose
\(C=E_{i,d}\), \(D=E_{d,j}\). Both separate compressions
are zero, whereas \(c_0(CD)=E_{i,j}\).
Thus even the most elementary excursion forbids treating
the retraction as a local crossing replacement or tensor
functor. The proof states this limitation explicitly.

The resulting representative is supported on the
\(A\ne1\) cut chart. Other geometric chart divisors and
the internal Gaussian/source map remain separate.

## 4. Additional check of the off-root product and pivot moment

The two-normal distinction in
[the complete-color divided Ward note](complete_color_divided_ward_and_fusion.md),
section 7, also checks directly. In the generic balanced lift,
\[
 \epsilon_a=MQ^{-a-1}-M^{-1},\qquad
 F_{a+1,a}=1-Q^{a+1}.
\]
Subtracting adjacent diagonal products gives the usual
\(\rho(K-K^{-1})\) at every interior vertex. The absent
last edge leaves exactly
\[
 [\mathcal E,F]-\rho(K-K^{-1})
 =-(1-Q^N)(MQ^{-N}-M^{-1})E_{N-1,N-1}.
\]
Hence the root wall and the integral-color wall are
different normals, even though the defect vanishes on both.

On the integral color \(m=N-1\), each of the \(b-1\)
closed pivot ratios contributes
\(q^{-Nm+2Na_j}\). The inverse-writhe twist ratio contributes
\(q^{Nm\ell}\). Their product is exactly
\[
 q^{Nm(\ell-b+1)+2N\sum_{\mathrm{closed}}a_j}.
\]
Knot parity makes its root value one. Its logarithmic
derivative still contains the closed-position moment;
there is no equality of off-root jets merely from the
root scalar equality. The current notes retain that
moment and use the genuine generic pivot before divided
specialization, so no adapter is omitted.
