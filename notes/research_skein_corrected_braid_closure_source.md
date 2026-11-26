# Actual skein-corrected mixed closure rows for the pointed braid source

Private written proof, 19 November 2026.

The based quantum meridian matrices are exact fundamental-probe
monodromies after one fixed auxiliary change of basis. This gives an
actual link realization of every fixed matrix word, including the
mixed closure traces. A finite homotopy in the closed-braid complement
then expresses each mixed closure source as
\(q^{1/2}-q^{-1/2}\) times finitely many specified decorated sources.
The crossing resolutions, framings, original cut, finite caps and
whole meridian family remain in that identity.

The small coefficient is an algebraic divisibility statement.
No bound on the decorated sources, geometric cycle coefficient,
or multiplicative descent of the original functional follows.

The complete directs are P, the actual fundamental fusion and
pivotal conventions; S, the based quantum separator; and B, the
marked braid-axis closure and pointed source. All new matrix,
homotopy and source calculations are below.

## 1. Parameters, the actual cut, and the probe

Fix
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 \rho=q-q^{-1},\quad A=q^{1/2}=e^{\pi i/(2N)},\quad
 \delta=A-A^{-1}.
 \tag{1}
\]
The square root is marked as displayed. Keep \(q\) fixed and vary
the physical meridian \(M=e^\mu\), with \(x=-M/q\).
On each balanced physical head,
\[
 Kw_a=xQ^{-a}w_a,\quad
 Fw_a=(1-Q^{a+1})w_{a+1},\quad
 Ew_a=(MQ^{-a}-M^{-1})w_{a-1}.
 \tag{2}
\]
The two arrows leaving \(0,\ldots,d\) are zero. In particular the
formula for \(E\) is used only for \(a>0\).
These matrices obey
\[
 KE=QEK,\quad KF=Q^{-1}FK,\quad
 [E,F]=\rho(K-K^{-1}).
 \tag{3}
\]
Ordered totals are \(E_{AB}=E_AK_B+E_B\),
\(F_{AB}=F_A+K_A^{-1}F_B\), and \(K_{AB}=K_AK_B\).

Let \(\beta\) be any fixed \(m\)-head braid, \(m\ge2\), and let
\(W_\beta(M)\) be its actual operator, including every physical
crossing scalar. Its specified pointed source is
\[
 \Phi_M(X)=\operatorname{Tr}
       ((P_0\otimes K_{\rm r}^{1-N})X),
 \tag{4}
\]
where \(P_0\) is the first-head vacuum projector and \({\rm r}\)
denotes the remaining \(m-1\) heads. Any prescribed zero-framing
or dimension line outside (4) is retained as the same multiplier
of every identity below.

The auxiliary color is the actual two-dimensional fundamental
module \(V_{\rm f}\), with \(E_{\rm f}w_1=w_0\),
\(F_{\rm f}w_0=w_1\), and Cartan eigenvalues \(q,q^{-1}\).
P fixes
\[
 g_{\rm f}=-\operatorname{diag}(q,q^{-1}),\qquad
 \theta_{\rm f}=-q^{3/2}=-A^3.
 \tag{5}
\]
Closing an auxiliary factor on the left uses \(g_{\rm f}^{-1}\),
not \(g_{\rm f}\). Its invariant cup and cap give an operator
\(e\) on two auxiliary strands with
\[
 e^2=-(q+q^{-1})e,\quad
 \check R_{\rm ff}=A I+A^{-1}e,\quad
 \check R_{\rm ff}^{-1}=A^{-1}I+A e.
 \tag{6}
\]
Thus, including the orientation and framing of the two smoothings,
\[
               \check R_{\rm ff}-\check R_{\rm ff}^{-1}
                         =\delta(I-e).
 \tag{7}
\]
The identities hold also at \(N=2\); no auxiliary projector
with a vanishing quantum-dimension denominator is introduced.

## 2. Exact mixed half-crossings and the based matrices

Use the retained unrolled logarithm to define \(K^{1/2}\) on a
physical head. The auxiliary color is first, the physical color
second. Remove only the permutation from each mixed crossing.
In the standard auxiliary basis the two half-crossings are
\[
 U^{\rm old}=
 \begin{pmatrix}K^{1/2}&\rho K^{1/2}F\\0&K^{-1/2}\end{pmatrix},
 \qquad
 V^{\rm old}=
 \begin{pmatrix}K^{1/2}&0\\
        \rho K^{-1/2}E^{\rm old}&K^{-1/2}\end{pmatrix}.
 \tag{8}
\]
Here \(E=\rho^2E^{\rm old}\). This follows by changing from the
ordinary highest-weight basis to \(w_a=v_a/f_a\), where
\(f_a=\prod_{j=1}^a(1-Q^j)\). Explicitly
\([a]/(1-Q^a)=-q^{-a}/\rho\), which gives (2) from P's ordinary
lowering coefficient. Formula (8) is the actual finite
Cartan-times-Euler crossing: only transfer zero or one can occur
on the fundamental factor. All common mixed Cartan scalars are
already in the displayed \(K^{\pm1/2}\).

Conjugate all auxiliary coordinate matrices by the same
\(D=\operatorname{diag}(\rho^{-1},1)\), using
\(U=D U^{\rm old}D^{-1}\) and \(V=D V^{\rm old}D^{-1}\)
on all its strand segments.
For every fixed \(N\), \(\rho\ne0\). The matrices become
\[
 U=\begin{pmatrix}K^{1/2}&K^{1/2}F\\0&K^{-1/2}\end{pmatrix},
 \qquad
 V=\begin{pmatrix}K^{1/2}&0\\K^{-1/2}E&K^{-1/2}\end{pmatrix}.
 \tag{9}
\]
Their inverses have bounded Laurent-polynomial entries as well.
The transformed cups and caps are used consistently, so the
basis changes cancel on every closed auxiliary component.
No inverse power of \(\rho\) remains in (9) or its inverses.

The positive monodromy with the auxiliary factor first is \(T=VU\).
Since \(K^{-1/2}EK^{1/2}=q^{-1}E\),
\[
 T=\begin{pmatrix}
       K&KF\\q^{-1}E&q^{-1}EF+K^{-1}
    \end{pmatrix}.
 \tag{10}
\]
Now use S's exact matrices
\[
 L^+=\begin{pmatrix}K&qE\\0&1\end{pmatrix},\quad
 L^-=\begin{pmatrix}1&0\\-KF&K\end{pmatrix},\quad
 G=(L^-)^{-1}L^+,\quad
 J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
 \tag{11}
\]
All products keep their operator order. Direct multiplication gives
\[
 (L^+)^{-1}L^-=
 \begin{pmatrix}
 K^{-1}+q^{-1}EF&-q^{-1}E\\-KF&K
 \end{pmatrix}.
 \tag{12}
\]
Here \(K^{-1}EK=Q^{-1}E\) was used, without commuting \(E\) and
\(F\). Consequently
\[
             T=J^{-1}G^{-1}J,\qquad
             U=K^{-1/2}J^{-1}L^-J
 \tag{13}
\]
are exact finite identities, not only principal-symbol identities.

Put \(U_{<i}=U_{i-1}\cdots U_1\). The negative based probe goes
past the earlier heads, winds negatively around head \(i\), and
returns along that same path. Its exact operator is
\[
 \mathcal M_i=U_{<i}^{-1}T_i^{-1}U_{<i}.
 \tag{14}
\]
The permutation of factor positions is understood in the actual
mixed crossings; (14) is their expression after returning the
auxiliary factor to the first position. Different physical heads
commute, so
\[
 U_{<i}=(K_{i-1}\cdots K_1)^{-1/2}
                  J^{-1}(L_{i-1}^-\cdots L_1^-)J.
 \tag{15}
\]
The scalar half-Cartan factor in (15) commutes with \(T_i\)
and cancels in (14). Therefore, with S's based quantum meridian,
\[
 \boxed{\quad
 \mathcal M_i=J^{-1}H_iJ,\qquad
 H_i=(L_{i-1}^-\cdots L_1^-)^{-1}G_i
                         (L_{i-1}^-\cdots L_1^-).
 \quad}\tag{16}
\]
In particular every fixed word in the \(\mathcal M_i^{\pm1}\)
has a Laurent expression of bounded degree, independent of \(N\),
in the physical \(E,F,K^{\pm1}\). The apparent half-Cartans and
inverse \(\rho\) have disappeared. These identities hold on the
actual caps and throughout the original meridian family.

For a free word \(\gamma\) in letters \(h_i^{\pm1}\), evaluate it
in this fixed product order to obtain \(\mathcal M_\gamma\) and
\(H_\gamma\). Closing the first auxiliary factor gives exactly
\[
 \operatorname{ptr}_{\rm f}^{\,L}(\mathcal M_\gamma)
 =\operatorname{Tr}_{\rm f}(g_{\rm f}^{-1}\mathcal M_\gamma)
 =-\operatorname{tr}_q(H_\gamma),\qquad
 \operatorname{tr}_q B=qB_{11}+q^{-1}B_{22}.
 \tag{17}
\]
Indeed conjugating \(g_{\rm f}^{-1}\) by \(J\) gives
\(-\operatorname{diag}(q,q^{-1})\).
Each probe is an actual pure braid on the auxiliary and physical
strands and hence a total intertwiner on their combined tensor.
P's literal pivotal contraction makes (17) a total physical
intertwiner. This proves that property for every fixed word,
not only for a single or an initial-block Casimir trace.

## 3. Exact braid covariance and the mixed source moment

The probes have S's inverse-Hurwitz convention. One can check the
sign without a classical limit. On an auxiliary strand and two
physical strands write \(a\) for the first mixed crossing and
\(b\) for the physical crossing. The two negative based probes are
\[
                  \mathcal M_1=a^{-2},\qquad
                  \mathcal M_2=a^{-1}b^{-2}a.
 \tag{18}
\]
These expressions denote the corresponding colored braid paths.
The adjacent braid relation gives
\(bab^{-1}=a^{-1}ba\), and therefore
\(b\mathcal M_1b^{-1}=\mathcal M_2\).
It also gives
\[
 b(a b^2a)=(a b^2a)b.
 \tag{19}
\]
Since \(\mathcal M_2\mathcal M_1=(a b^2a)^{-1}\), it follows that
\[
 \operatorname{Ad}_b(\mathcal M_1,\mathcal M_2)
   =(\mathcal M_2,\mathcal M_2\mathcal M_1\mathcal M_2^{-1}).
 \tag{20}
\]
Earlier based paths conjugate this calculation; later paths are
unchanged because the total loop about the two heads is preserved.
Thus for every actual braid word
\[
 \operatorname{Ad}_{I_{\rm f}\otimes W_\beta}\mathcal M_\gamma
                       =\mathcal M_{\beta(\gamma)}.
 \tag{21}
\]
Equivalently, this follows from (16) and S's four-entry quantum
Hurwitz identity. All actual scalar crossing factors cancel in
this conjugation only; they remain in the source.

For any fixed word \(w\), define the bounded physical operator
\[
 R_{i,w}=
       \operatorname{tr}_q\bigl((H_{\beta(h_i)}-H_i)H_w\bigr)
 =\operatorname{tr}_q\bigl((\operatorname{Ad}_{W_\beta}H_i-H_i)H_w\bigr).
 \tag{22}
\]
It is a genuine whole-meridian total intertwiner by (17).
Let \(L_{\gamma;\beta}\) be the actual auxiliary link obtained by
placing the probe \(\mathcal M_\gamma\) above the core braid
\(W_\beta\), closing the first auxiliary strand on the left, and
making the prescribed pointed/pivotal closure of the physical
braid. Write \(\mathcal F_\beta(L;M)\) for that decorated source
with the same physical scalars as (4). For these endpoint probes,
\[
 \mathcal F_\beta(L_{\gamma;\beta};M)
                  =-\Phi_M(\operatorname{tr}_q(H_\gamma)W_\beta).
 \tag{23}
\]
The auxiliary strand is a single monotone strand in the probe
braid. Its closure outside the braid projection introduces no
self-crossing. Its blackboard self-framing is therefore zero.
Crossings with the physical strands are retained and do not
enter that self-framing count.

In particular, setting \(\gamma_+=\beta(h_i)w\) and
\(\gamma_-=h_iw\), equations (22)--(23) give
\[
 \mathcal F_\beta(L_{\gamma_+;\beta};M)
 -\mathcal F_\beta(L_{\gamma_-;\beta};M)
                         =-\Phi_M(R_{i,w}W_\beta).
 \tag{24}
\]

## 4. The finite auxiliary homotopy and its framing correction

The closed-braid complement has the usual literal closure
relations \(\beta(h_i)=h_i\) in this convention. They can be
checked by keeping a based puncture loop in the open braid:
transport through the braid gives \(\beta(h_i)\), and closure
identifies its top and bottom base paths. Equivalently, form the
group with a stable letter \(t\) and
\(t h_i t^{-1}=\beta(h_i)\), then impose \(t=1\) for this closure.
Using the contravariant physical point convention replaces
\(\beta\) by its inverse and gives the same set of literal fixed
relations. No sign of the physical full twist is changed here.

It follows that the two specified auxiliary loops in (24) are
homotopic in the complement of the fixed physical closed braid.
Choose one such homotopy. A finite smooth approximation, followed
by a perturbation relative to its embedded endpoints, makes it
generic: between finitely many isolated double-point times the
loop is embedded, and at each double-point time just two
auxiliary arcs pass through one another transversely. This is
the usual dimension count for a one-parameter family of curves
in a three-manifold. The compact homotopy stays a positive
distance from the physical core, so the approximation and
perturbation never cross that core. Embedded intervals extend
to ambient isotopies by extending their velocity in a tubular
neighborhood. Thus the homotopy is a finite succession of
ambient isotopies and auxiliary crossing changes.

Track the ribbon framing through this succession. Ambient
isotopies preserve its self-linking. At an auxiliary crossing
change, comparison with the blackboard ribbon on the other
side changes self-linking by \(+2\) or \(-2\): the two
strand/push-off crossings in the linking count change together.
Since both endpoint probes in (24) have zero self-framing, the
carried final ribbon differs from the specified endpoint by
an even number \(2h\) of twists. This parity assertion is
essential because \(\theta_{\rm f}\) tends to \(-1\), not \(1\).

At each crossing event (7) replaces the difference by
\(\delta\) times two actual smoothed diagrams. Their inherited
framings and all other strands are kept. The final even repair
also has this divisibility:
\[
 \theta_{\rm f}^{\,2h}-1=A^{6h}-1
                   \in \delta\,\mathbb Z[A,A^{-1}].
 \tag{25}
\]
For instance \((A^6-1)/\delta=A(1+A^2+A^4)\); negative \(h\)
is handled by multiplication by a Laurent unit. Equivalently
one may restore zero framing after each crossing change, using
the same even-twist identity at each step.

Telescoping the finite succession therefore proves a literal
framed skein identity
\[
 L_{\gamma_+;\beta}-L_{\gamma_-;\beta}
                       =\delta\sum_{j=1}^{J}c_j(A)L_j,
 \qquad c_j(A)\in\mathbb Z[A,A^{-1}].
 \tag{26}
\]
Here \(J\), all diagrams, and all Laurent degrees are fixed by
the chosen finite braid, word, and homotopy, independently of
\(N\) and \(M\). A smoothing may split an auxiliary component;
all resulting components carry the actual fundamental color.
The diagrams \(L_j\) retain the original physical core. They
may contain auxiliary stages at several heights of that core
and may have nonzero inherited framings. They are not replaced
by arbitrary initial-cut coupons or by unframed group words.

Equation (26) is not a claim that homotopic loops are equal at
generic \(q\). It is their explicit finite skein correction,
proved from (7) and (25).
The Laurent variable \(A\) records the diagrammatic coefficients;
the actual finite evaluation is at (1). No off-root deformation
of a fixed-\(N\) capped representation is asserted.

## 5. The exact original-source closure row and its normal

Evaluate (26) with the actual finite matrices of P and the
pointed/pivotal source (4). Framed isotopy, the two local
smoothings in (7), and twists in (25) are identities of those
same matrices and cup/cap contractions. With (24), the result is
\[
 \boxed{\quad
 \Phi_M(R_{i,w}W_\beta)
             +\delta\sum_{j=1}^{J}c_j(A)\,
                          \mathcal F_\beta(L_j;M)=0.
 \quad}\tag{27}
\]
This is an actual equality at every level \(N\ge2\), throughout
the original meridian germ. All physical and fundamental sums
have their finite endpoints. No Gaussian-factorial denominator
at index \(N\), cyclic replacement of a capped arrow, or
singular auxiliary fusion projector occurs in the proof.

All coefficients in (27) are independent of \(M\). It follows
by differentiating the finite equality, for every fixed
nonnegative integer \(a\), that
\[
 \left.\partial_\mu^a\Phi_{e^\mu}(R_{i,w}(e^\mu)W_\beta(e^\mu))
       \right|_{\mu=0}
 +\delta\sum_j c_j(A)
       \left.\partial_\mu^a\mathcal F_\beta(L_j;e^\mu)
       \right|_{\mu=0}=0.
 \tag{28}
\]
These derivatives include the cut pivot, all original crossing
scalars and the moving physical arrows. If an outside normalization
line is prescribed, multiply it into every term of (27) before
differentiating; its derivatives then remain by the product rule.
If a reduced prefix formula expresses the
source through a meromorphic Cartan factor, its finite part
is taken only after the full equality; its residue and moving
first coefficients are not dropped. The actual source (4)
and its decorated versions supply the regular finite expression.

The initial mark (22) is an intertwiner, so its total Ward
commutators vanish identically. This removes the forced
nonintertwiner terms for that mark. It does not remove the
resolved-link terms in (27). Cyclicity of the invariant pointed
trace alone gives only the twisted commutator rows in B;
the auxiliary homotopy and its framing data are additional
source-specific input.

## 6. Classical closure equations and the precise remaining scope

On the complete-root coherent charts of S, explicitly at \(M=1\),
a fixed Laurent
word has its computed commutative principal substitution.
Equations (16)--(17) therefore give, for every fixed word,
the classical endpoint trace \(-\operatorname{tr}(H_\gamma)\).
In particular the principal of (22) is
\[
 r_{i,w}=\operatorname{tr}\bigl(((\beta H)_i-H_i)H_w\bigr).
 \tag{29}
\]
The finite skein row (26) has \(\delta=0\) at the diagrammatic
specialization \(A=1\); its two endpoint expressions are then
the mixed closure difference with the sign in (24).
This is an algebraic specialization, together with S's paid
root symbol of the bounded endpoint mark.

Choose the four basis words \(w=w_\nu\) of an irreducible
trace-Gram chart, so their matrices are
\((I,H_a,H_b,H_aH_b)\) or \((I,H_a,H_b,H_c)\).
The inverse Gram matrix reconstructs each
\((\beta H)_i-H_i\) from the four traces (29). Hence the
resulting classical equations cut out literal ordered closure
on this chart, including its local Artin directions. On the
regular-total eigenvalue cover of B they are precisely the
additional marked condition \(z_\beta=1\) within the
character-fixed locus. Thus (27) supplies actual finite
source rows with these closure leading expressions; they are
stronger data than invariant trace fixedness alone.

No numerical estimate of the second term of (27) follows from
\(\delta=O(N^{-1})\). Its decorated sources can have their own
large asymptotics and normal terms. The proof does not factor
them into bounded initial coupons, show that the staged
source module is flat in a semiclassical parameter, or make
the original functional descend multiplicatively to the
classical closure ring. The exact whole-meridian identity
(28) is also not a uniform meridian-normal symbol theorem.

In particular this result does not select a geometric factor
of a minimal annihilator, prove a nonzero coefficient of that
factor in the original relative cycle, or supply a lower
exponential bound. It supplies the specified actual closure
rows and all their finite source corrections for arbitrary
fixed braid words, without replacing the original scalar.

## 7. Background and proof dependency

The relation between specialized Kauffman skein modules and
\(SL_2\) characters is established background; see the primary
abstracts of [Bullock](https://arxiv.org/abs/q-alg/9604014) and
[Przytycki--Sikora](https://arxiv.org/abs/q-alg/9705011).
The former describes the character ring after quotienting the
specialized module by its nilradical; the latter describes the
unreduced character algebra at \(A^2=1\).
No novelty is claimed for that framework or for the crossing-change
argument. No theorem or proof from those papers is imported here.
The present \(A\to+1\) sign is fixed by the exact probe and left
pivot in (16)--(17), rather than by substituting an unmarked
skein-character convention. The explicit matrix and homotopy
derivations above preceded this abstract-level coverage check.

## Complete proof-source pins

* P: notes/actual_peripheral_fusion.md,
  SHA256 cee06548a794b0adfe56a289be7d5972c80be17dc41d854075a135473bd8959a
  (427 lines).
* S: notes/research_finite_trace_separator_and_opposite_characteristic.md,
  SHA256 1d5abd4e14df7aa32f17405e27543a35d815c130903ed379ab9c60bec2eef0f6
  (561 lines).
* B: notes/research_braid_axis_closure_multiplier.md,
  SHA256 0c473ffed9a15cc8193b73a0323cd9058986e56dfc47731470a72ac764be34e0
  (510 lines).

All three complete directs were read nontruncated in the active
author sequence. P was freshly reread in two covering chunks;
the complete matching S and B reads were retained unchanged
from the immediately preceding separator and axis author sequence.
Only written mathematics, text/hash operations, and the stated
primary-abstract coverage check were used.
Frozen and public files were not changed.
