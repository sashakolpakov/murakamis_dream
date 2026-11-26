# Root-orbit cap observations and retained-face operators

Private written proof, 17 November 2026. Taking the full root orbit
of the phased cap, together with its Jackson moments, detects
exactly the attachment degrees at least \(N-1\). The joint invisible
space is preserved by the two literal retained-face Casimir
operators. This gives an exact larger observation module with
explicit transitions and original signed crossing actions.
It does not permit arbitrary neighboring multiplication or
elimination of another face, and supplies no scalar lower bound.

## 1. The entire orbit and its exact kernel

Use the fixed-root conventions of [M], with
\[
 N\ge3,\quad d=N-1,\quad q=e^{\pi i/N},\quad
 \sigma=\pm1,\quad \omega=q^\sigma,\quad
 \tau=\omega^2,\quad a=-\omega,\quad a_j=a\tau^j.
 \tag{1}
\]
Let \(\mathcal B\) contain an independent external variable \(z\)
and all other attachment parameters; \(z\) is distinct from
\(c,y\) in this representation. Work on
\[
 E_N=\mathcal B[c,y]/(c^N,y^N),\qquad
 \ell_b(F)=[t^d]F(bt,t),\qquad
 m_r(b;F)=\ell_bD_{\tau,c}^rF,\quad 0\le r\le d.
 \tag{2}
\]
The phase observations are \(m_{r,j}(F)=m_r(a_j;F)\).
All phases are kept; the original protected-zero cap closing is
still \(\lambda m_{0,0}\), with \(\lambda=q^{\sigma d^2/2}\) on its
original lift. As in [M], restored probe variables can be taken
independently of attachment parameters before specialization.

Write \(F=\sum_{i,k=0}^df_{ik}c^iy^k\). Directly,
\[
 m_r(b;F)=
 \sum_{k=0}^{d-r}
   f_{r+k,d-k}\frac{[r+k]_\tau!}{[k]_\tau!}b^k.
 \tag{3}
\]
Thus each row polynomial has degree at most \(d-r\), and the
complete root orbit recovers every coefficient in that band:
\[
 f_{r+k,d-k}
 =\frac{[k]_\tau!}{[r+k]_\tau!}\,
    \frac{a^{-k}}N\sum_{j=0}^d\tau^{-jk}m_{r,j}(F).
 \tag{4}
\]
All factorial indices are less than \(N\). No semisimple spectral
replacement is used; this is ordinary finite Fourier inversion
of the exact cap moments.

It follows that their common kernel and quotient are
\[
 L_{<d}=\operatorname{span}_{\mathcal B}
       \{c^iy^k:i+k<d\},\qquad
 V_N=E_N/L_{<d},\qquad
 \operatorname{rank}_{\mathcal B}V_N=\frac{N(N+1)}2 .
 \tag{5}
\]
The \(N^2\) displayed observations are redundant: in band \(r\)
only Fourier frequencies \(0,\ldots,d-r\) occur. Formula (4)
is an explicit inverse onto precisely that constrained array.
Compared with the single-phase quotient [M], this retains all
high-degree coefficients, not only one linear combination in
each degree.

The identity \(\ell_{a_j}=\ell_a S_c^j\), where
\(S_cF(c,y)=F(\tau c,y)\), identifies \(j\) as an ordinary-face
coefficient-clock character. It is not an external circle color
or a replacement of the original marked cut. In particular no
equality of the scalar observations at different \(j\) is asserted.

## 2. Literal Casimir operators on the quotient

Let \(T_y\) be the operator of [F] with middle variable \(y\)
and outer variables \(c,z\). Its exact polynomial formula is
\[
\begin{split}
 T_y(c^iy^k)
  &=A_kc^iy^k+b_kc^{i+1}y^{k-1}
       +zb_kc^iy^{k-1}+ze_kc^{i+1}y^{k-2},\\
 A_k&=-(\omega\tau^k+\omega^{-1}\tau^{-k}),\\
 b_k&=2-\tau^k-\tau^{-k},\\
 e_k&=\omega+\omega^{-1}
             -\omega\tau^{-k}-\omega^{-1}\tau^k .
\end{split} \tag{6}
\]
These coefficients are unchanged when \(\sigma\) is reversed.
The apparent negative powers in (6) have zero coefficients:
\(b_0=e_0=e_1=0\). All coefficients are \(N\)-periodic, so
\(T_y(y^NF)=y^NT_yF\); multiplication by \(c^N\) also commutes.
Thus the actual operator preserves the defining ideal of \(E_N\).
The operator \(T_c\) is obtained by interchanging \(c,y\), with
the same external \(z\).

Both operators preserve or lower total \(c,y\)-degree. They
therefore preserve \(L_{<d}\), unlike the single-phase kernel
in [M]. With
\[
 E_{r,i}=c^iy^{d+r-i},\qquad 0\le r\le d,\quad r\le i\le d,
 \tag{7}
\]
their complete quotient matrices are
\[
\begin{split}
 T_yE_{r,i}
  &=A_kE_{r,i}+b_kE_{r,i+1}
          +zb_kE_{r-1,i}+ze_kE_{r-1,i+1},
       &&k=d+r-i,\\
 T_cE_{r,i}
  &=A_iE_{r,i}+b_iE_{r,i-1}
          +zb_iE_{r-1,i-1}+ze_iE_{r-1,i-2}.
\end{split} \tag{8}
\]
Every index outside (7) means zero. This convention retains both
the \(c^N,y^N\) endpoints and the invisible lower-degree boundary.
The external \(z\) remains an actual coefficient variable:
its later prescribed coefficient extraction is unchanged.

If the literal outer faces coincide, substitute before taking
moments. For example \(z=c\) in \(T_y\) gives instead
\[
 T_yE_{r,i}=A_kE_{r,i}+2b_kE_{r,i+1}+e_kE_{r,i+2}.
 \tag{8a}
\]
It still preserves the same lower-degree kernel, but (9) below
cannot be used by treating \(z\) as constant and only afterwards
setting \(z=c\). The analogous \(T_c\) coincidence is \(z=y\).
Identification of a middle face with its outer face is outside
the literal chart of [F].

Equation (8) is an explicit representation of the source-normalized
operators \(T=-\Omega\) of [F], on arbitrary polynomial attachments
in the stated variables. Products of these two operators act in
their literal order, on all current coefficients. No commutation
or reordering of actual ports is implicit.

## 3. Exact transitions in the cap-row coordinates

The same action has a local expression in the phase orbit.
Let \(Sg(b)=g(\tau b)\), and put \(m_N=0\). All \(b\)'s below
multiply on the left of the indicated shifts. Then
\[
\begin{split}
 m_r(b;T_yF)
 &=\mathcal L_{y,r}m_r(b;F)
       +z(1-\tau)\mathcal B_{y,r}m_{r+1}(b;F),\\
 \mathcal L_{y,r}
 &=-\omega S-\omega^{-1}S^{-1}
       +b\bigl(1+\tau^r-\tau^{r+1}S-\tau^{-1}S^{-1}\bigr),\\
 \mathcal B_{y,r}
 &=b(1-\tau^{-1}S^{-1})
       +\omega b^2(\tau^r-\tau^{-2}S^{-1}),
\end{split} \tag{9}
\]
and
\[
\begin{split}
 m_r(b;T_cF)
 &=\mathcal L_{c,r}m_r(b;F)
       +z(1-\tau)\mathcal B_{c,r}m_{r+1}(b;F),\\
 \mathcal L_{c,r}
 &=-\omega\tau^rS-\omega^{-1}\tau^{-r}S^{-1}
       +b^{-1}(1+\tau^{-r}-S-\tau^{-r}S^{-1}),\\
 \mathcal B_{c,r}
 &=1-\tau^{-r-1}S^{-1}
       +\omega\tau^{-r-1}b^{-1}(1-S^{-1}).
\end{split} \tag{10}
\]
The numerators accompanying \(b^{-1}\) kill constants, so (10)
is polynomial on the permitted row polynomials. At \(b=a_j\),
\(S^{\pm1}\) simply shifts \(j\) modulo \(N\).

For completeness, on a preserving input band put
\(i=r+k,\ j=d-k\). Relative to its coefficient in \(m_r\),
the non-diagonal preserving factors in (9) and (10) are respectively
\[
 b(1-\tau^{r+k+1})(1-\tau^{-k-1}),\qquad
 b^{-1}(1-\tau^k)(1-\tau^{-r-k}).
 \tag{11}
\]
On an input band \(r+1\), the two \(z\)-factors relative to
the coefficient in \(m_{r+1}\) are, for \(T_y\),
\[
 (1-\tau)b(1-\tau^{-k-1}),\qquad
 \omega(1-\tau)b^2(\tau^r-\tau^{-k-2}),
 \tag{12}
\]
and for \(T_c\),
\[
 (1-\tau)(1-\tau^{-r-k-1}),\qquad
 \omega(1-\tau)\tau^{-r-1}b^{-1}(1-\tau^{-k}).
 \tag{13}
\]
These follow by canceling the allowed factorial ratios in (3).
At the potential \([N]_\tau\) endpoint use the original zero
coefficient in (6): the final factor in (12) vanishes at
\(k=d-r-1\), and the \(k=0\) term in (13) is zero.
The top \(b\)-raising coefficient in (11) vanishes at \(k=d-r\).
Thus (9)--(10) preserve every degree bound in (3), including all
truncated endpoints, without dividing by a zero factorial.

## 4. Full Hermite coupons and signed crossing powers

The Casimir sign must be retained. Put
\[
 \mathcal P_N(u)=2\,\operatorname{ChebT}_N(u/2)+2,\qquad
 \chi_N(t)=\prod_{j=0}^d(t-A_j)
        =2\,\operatorname{ChebT}_N(t/2)+2(-1)^N .
 \tag{14}
\]
For either \(v=c,y\),
\[
 \chi_N(T_v)=0,\qquad \mathcal P_N(-T_v)=0
 \quad\hbox{on }E_N\hbox{ and }V_N.
 \tag{15}
\]
One direct proof uses the filtration by the middle exponent:
\(T_v-A_j\) lowers its \(j\)-th layer. Applying these factors
in descending order kills the entire filtration, and they
commute because all are polynomials in \(T_v\).
Equivalently this is the full-block annihilator proved in [S].
The parity in (14) follows from
\(\chi_N(t)=(-1)^N\mathcal P_N(-t)\).

Let \(r_{N,+}\) be the original normalized crossing polynomial
and \(r_{N,-}\) its inverse modulo \(\mathcal P_N\), as in [S].
The literal signed operators on the retained-face quotient are
\[
 \mathcal R_{v,\epsilon}
   =\kappa^\epsilon r_{N,\epsilon}(-T_v),
 \qquad \epsilon=\pm1,\qquad \kappa=q^{d^2/2}.
 \tag{16}
\]
The original lift of \(\kappa\), and all Hermite derivatives at
repeated nodes, are kept. Equations (15)--(16) give inverse
operators, not merely inverse nodal values. Every word in these
specified retained-face operators and their Casimir coupons
therefore has its exact action on (5), followed by the unchanged
row \(\lambda m_{0,0}\). This is a local operator representation;
it does not assert that an arbitrary diagram elimination uses
only these retained variables or these two operator placements.

In fact no Hermite direction for either single Casimir is lost.
On the lowest visible degree band, (8) becomes the opposite
bidiagonal matrices displayed below, whose off-diagonal entries
are nonzero. An endpoint vector is cyclic, so their minimal
polynomial has degree \(N\). Thus (15) is the full minimal
polynomial there, including its repeated roots.

There is an honest coefficient-norm bound. On the high-degree
basis use the inherited weighted \(\ell^1\) norm with positive
radii \(r_c,r_y,r_z\). It is exactly the original coefficient
norm restricted to that basis, since (5) discards disjoint
monomials. Formula (6) gives
\[
 \|T_y\|\le C_y=
 2+4(r_c+r_z)/r_y+4r_cr_z/r_y^2,
 \tag{17}
\]
and the \(c\)-bound interchanges \(r_c,r_y\).
This also holds on a complex \(z\)-fiber with \(|z|\le r_z\).
The small-circle recurrence gives
\(\|P_{h-1}(T_y)\|\le(C_y+1)^{h-1}\).
A polynomial of fixed degree with uniformly bounded coefficients
therefore has bounded cost independent of \(N\).
A fixed crossing exponent is a different matter:
already one signed crossing uses the full degree-\(d\) Hermite
polynomial of [S].
Neither (17) nor the explicit factor \(1-\tau\) in (9) proves
a polynomial crossing norm or a small inter-band coupling in
the unnormalized moment coordinates.

In fact the exact single-crossing norm on this quotient still
has the full exponential rate. With unit coefficient weights
\(r_c=r_y=r_z=1\), for either \(v=c,y\) and either sign,
\[
 \log\|\mathcal R_{v,\epsilon}\|_{V_N,1}
      =NG_*+O(\log N),\qquad
 G_*=-4\int_0^{1/4}\log(2\sin\pi t)\,dt
      =\frac{v_{\rm oct}}{2\pi},
 \tag{17a}
\]
where \(v_{\rm oct}\) is the regular ideal octahedron volume.
This norm retains the polynomial coefficients in the external
\(z\), as well as the visible \(c,y\) coefficients.

Here is a source-exact lower bound at every sufficiently large
level. Set \(m=\lfloor N/4\rfloor\). The unit-norm input
\(c^{3m}y^{d-2m}\) belongs to visible band \(r=m\).
The original multinomial formula [S, (4)] for the crossing in
the \(c\)-face has exactly one term with output
\[
 c^m y^{d-m}z^m,\qquad
 |\text{coefficient}|=\frac{S_{3m}}{S_m^3},
 \qquad S_j=\prod_{\nu=1}^j2\sin(\pi\nu/N).
 \tag{17b}
\]
Indeed its three multinomial allocations must all equal \(m\).
The input exponents are less than \(N\), and the output has
total \(c,y\)-degree \(d\), with both exponents less than \(N\).
Thus neither quotient operation removes it. The coefficient has
the same modulus for both crossing signs; the actual \(\kappa\)
factor has modulus one. The uniform sine-product estimate of [S]
gives \(\log(S_{3m}/S_m^3)=NG_*+O(\log N)\).

For the matching upper bound, the full original polynomial crossing
has norm \(K_N(1,1)\) from [S, (9)], with
\(\log K_N(1,1)=NG_*+O(\log N)\) by its rate and symmetric
four-angle maximum. Passing to this coefficient quotient is
nonexpansive. Swapping \(c,y\) proves the same statement for the
other retained face. This proves (17a).
It is an operator norm calculation with an explicit polynomial
input, not a lower bound for an actual knot attachment or for
the final selected scalar.

## 5. Terminal phase rows and the original scalar

On the invariant bottom band put \(v_i=c^iy^{d-i}\) and
\[
 c_i=\omega\tau^i+\omega^{-1}\tau^{-i},\qquad
 \beta_i=\tau^i+\tau^{-i}-2.
 \tag{18}
\]
All terms with \(z\) drop into the discarded lower degrees.
The literal matrices are exactly
\[
 (-T_c)v_i=c_iv_i+\beta_iv_{i-1}=:Bv_i,\qquad
 (-T_y)v_i=c_iv_i+\beta_{i+1}v_{i+1}=B^{\mathsf T}v_i .
 \tag{19}
\]
Here \(\beta_0=\beta_N=0\), and all intermediate \(\beta_i\ne0\).
This defines the two matrices explicitly; no additional source
identification with a differently framed multiplicity model is used.

For \(F=\sum_{i=0}^df_iv_i\), write
\(\gamma_j=\ell_{a_j}F=\sum_i f_ia_j^i\).
Equations (9)--(10) at \(r=0\) give
\[
\begin{split}
 \gamma_j((-T_c)F)
  &=(\omega+a_j^{-1})\gamma_{j+1}
       +(\omega^{-1}+a_j^{-1})\gamma_{j-1}
       -2a_j^{-1}\gamma_j,\\
 \gamma_j((-T_y)F)
  &=(\omega+\tau a_j)\gamma_{j+1}
       +(\omega^{-1}+\tau^{-1}a_j)\gamma_{j-1}
       -2a_j\gamma_j .
\end{split} \tag{20}
\]
Although the phase labels use cyclic notation, the backward
coefficient is zero at \(j=0\) and the forward coefficient is
zero at \(j=d\), in both lines. Thus the finite endpoint is
literal and no phase-wrap term has been dropped.

For the complete original homogeneous attachment of [M], extracting
all other ordinary targets leaves total degree \(d\) in
\(X,Z,c,y\). Passing to (5) retains precisely
\(\sum_i f_ic^iy^{d-i}\), with no \(X,Z\) dependence.
The larger quotient retains its entire coefficient vector,
whereas the single-phase quotient kept only one combination.
The prescribed closing nevertheless remains exactly
\[
 \lambda\gamma_0=\lambda\sum_{i=0}^df_i a^i .
 \tag{21}
\]
Fourier recoverability and invertible signed operators do not
assert that this selected value is nonzero or determine its
exponential size.

The closure restriction is concrete. Multiplication by \(c\)
can send the invisible \(c^{d-1}\) to the visible \(c^d\).
Likewise an operator with middle variable \(z\) and outers \(c,y\)
does not preserve this quotient: applying its formula (6) to
\(c^{d-1}z\) produces the visible term
\(b_1(c^d+c^{d-1}y)\), with \(b_1\ne0\).
Thus this module closes the actual operators along its two
retained faces, not arbitrary face changes or global products.
All external targets and attachments must remain in their
original order. No off-root continuation, global invariant
quotient, or geometric lower bound is inferred.

## Complete direct sources and coverage

All three complete texts and used implications were read.
The ordered face-insertion, adjacent-observable, adaptive Fermat,
and charged-socle proofs were also read for coverage. They retain
different sources or observation families; none supplies (3)--(10).
No mathematical programs or numerical evaluations were used.

| Label | Source | SHA-256 |
|---|---|---|
| M | [Minimal restored-cap module](research_minimal_restored_cap_normal_module.md) | bf59e93e40c9e42baf34e19a504326909df6d15f57ab086845e7e969df1c88e0 |
| F | [Original polynomial face insertion](actual_small_circle_polynomial_face_insertion.md) | 57f6607e08074a72783af9e829bb2d16b596d7259f71aa91c0a6e500a3a25a3a |
| S | [Original signed face kernel](actual_signed_small_circle_face_kernel.md) | fa4aa7538ba4d44495e343b79fd0d21c58fb8f2558d27acdf9a4286774aeb60f |
