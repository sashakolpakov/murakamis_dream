# Finite trace observables for the opposite-polarization characteristic

Private written proof, 18 November 2026.

A finite explicit family of actual transported Casimirs separates the
ordered irreducible \(SL_2\) tuple up to one common conjugation. Both the
full operators and their first-head quotients have Laurent degree
bounded independently of the color \(N\). Their complete-root coherent
symbols can therefore be computed directly, without a symbol theorem
for a full crossing or the prefix change of basis.

Applied to the actual root kernel \(T(1)\) and the Laurent residue
of \(J\), these observables give explicit homogeneous characteristic
equations. They recover the turned ordered character and reverse
the selected regular total-product eigenvalue wherever such a
characteristic relation exists. The finite part of \(J\) instead
retains an inhomogeneous normal row. No nonzero kernel amplitude,
integration cycle, or geometric contribution is constructed.

The complete directs are M, the actual classical meridians; Q, the
literal rational quantum conjugation; R, the actual prefix quotient;
and J, the actual opposite-polarization kernel. All trace separation,
four-entry transport, and bounded-degree calculations are below.

## 1. Actual quantum based meridians

Fix \(N\ge2\), \(q=e^{\pi i/N}\), \(Q=q^2\), \(d=N-1\), and \(m\ge2\).
Keep the actual balanced generators, with \(E\) denoting the scaled
lowering operator:
\[
 KE=QEK,\qquad KF=Q^{-1}FK,\qquad
 [E,F]=(q-q^{-1})(K-K^{-1}).
 \tag{1}
\]
Different heads commute. Put \(e_i=qE_i\), and form matrices whose
entries are the actual finite operators:
\[
 L_i^+=\begin{pmatrix}K_i&e_i\\0&1\end{pmatrix},\qquad
 L_i^-=\begin{pmatrix}1&0\\-K_iF_i&K_i\end{pmatrix},\qquad
 G_i=(L_i^-)^{-1}L_i^+
   =\begin{pmatrix}K_i&e_i\\F_iK_i&F_ie_i+K_i^{-1}\end{pmatrix}.
 \tag{2}
\]
Only \(K_i\), an actual invertible diagonal matrix, is inverted.
For instance \((L_i^-)^{-1}=\left(\begin{smallmatrix}1&0\\F_i&K_i^{-1}
\end{smallmatrix}\right)\). Define the ordered prefixes and based
matrices by
\[
 B_j^\pm=L_j^\pm\cdots L_1^\pm,\qquad
 H_j=(B_{j-1}^-)^{-1}G_jB_{j-1}^-,\qquad B_0^\pm=I.
 \tag{3}
\]
All matrix products retain their noncommutative entry order.
Telescoping, without cyclically moving any entries, gives
\[
 H_s\cdots H_1=(B_s^-)^{-1}B_s^+.
 \tag{4}
\]
The ordered coproducts have
\[
 B_s^+=\begin{pmatrix}K_{[s]}&qE_{[s]}\\0&1\end{pmatrix},
 \quad
 B_s^-=\begin{pmatrix}1&0\\-K_{[s]}F_{[s]}&K_{[s]}\end{pmatrix}.
 \tag{5}
\]
For example the lower-left entry of \(L_2^-L_1^-\) is
\(-K_2F_2-K_2K_1F_1=-K_1K_2(F_1+K_1^{-1}F_2)\).
Induction proves (5). Thus with
\(\operatorname{tr}_q A=qA_{11}+q^{-1}A_{22}\),
\[
 \operatorname{tr}_q(H_s\cdots H_1)
 =F_{[s]}E_{[s]}+qK_{[s]}+q^{-1}K_{[s]}^{-1}
 =:\Omega_{[s]}.
 \tag{6}
\]
This fixes the normalization of every observable. Ordinary matrix
trace cyclicity has not been substituted for quantum trace.

### The four-entry checked-crossing calculation

Let \(\mathcal R\) be the literal positive checked crossing on two
equal-color heads, including its original scalar. The scalar cancels
in its conjugation action. Q's exact rational formulas, expressed
using the scaled \(E\), give
\[
 u=e_2K_2^{-1}K_1F_1,\quad
 G=(1-Q^{-1}u)^{-1},\quad Z=K_2(1-Q^{-1}u)=K_2-e_2K_1F_1,
 \tag{7}
\]
\[
 \operatorname{Ad}_{\mathcal R}K_1=Z,\qquad
 \operatorname{Ad}_{\mathcal R}e_1=e_2K_1,\qquad
 \operatorname{Ad}_{\mathcal R}F_1
       =F_1+F_2K_1^{-1}-GK_2^{-2}F_1=:F'.
 \tag{8}
\]
These are Q's algebra-conjugation formulas, rather than its
contravariant classical point map. On the actual root heads \(u^N=0\),
so every displayed inverse is an actual finite inverse. Its
degree-\(N\) expansion will not be used for a symbol calculation.

Direct multiplication gives
\[
 (L_1^-)^{-1}G_2L_1^-=
 \begin{pmatrix}
 Z&e_2K_1\\
 F_1Z+K_1^{-1}F_2K_2-F_2e_2F_1-K_2^{-1}F_1&
 e_2F_1K_1+F_2e_2+K_2^{-1}
 \end{pmatrix}.
 \tag{9}
\]
The first two entries agree with (8). For the third, the exact
relations \(F_1u=QuF_1\) and \(K_2^{-1}u=Q^{-1}uK_2^{-1}\) give
\[
 GK_2^{-2}F_1 Z
 =GK_2^{-1}(1-u)F_1=K_2^{-1}F_1.
 \tag{10}
\]
Consequently \(F'Z\) is the lower-left entry in (9). For the fourth,
\[
 F'e_2K_1+Z^{-1}
 =e_2F_1K_1+F_2e_2+
      G(K_2^{-1}-K_2^{-2}e_2F_1K_1).
 \tag{11}
\]
Here \(K_2^{-2}e_2F_1K_1=Q^{-1}uK_2^{-1}\), so the last summand is
\(K_2^{-1}\). This verifies all four entries and proves
\[
 \operatorname{Ad}_{\mathcal R}G_1=(L_1^-)^{-1}G_2L_1^-.
 \tag{12}
\]
The inverse denominators in (8) have cancelled in this observable.

Actual total intertwining preserves both products \(L_2^\pm L_1^\pm\).
Together with (4),(12), this proves the exact matrix rule
\[
 \operatorname{Ad}_{\mathcal R}(H_1,H_2)
       =(H_2,H_2H_1H_2^{-1}).
 \tag{13}
\]
The \(H_i\) are invertible products of triangular matrices, so this
step needs no scalar trace division. With earlier heads present,
conjugate (13) by their unchanged \(B^-_{i-1}\). Later prefixes stay
unchanged because \(L^-_{i+1}L^-_i\) is preserved. Thus the same
rule holds at any adjacent positions, fixing all other based matrices.
Its inverse is obtained by actual inverse conjugation.
The rule is the inverse Hurwitz action, as appropriate for
conjugation of observables.

## 2. A finite explicit family of transported Casimirs

For every increasing subset \(I=\{i_1<\cdots<i_s\}\), \(1\le s\le3\),
define
\[
 \mathcal O_I=\operatorname{tr}_q(H_{i_s}\cdots H_{i_1}).
 \tag{14}
\]
There is a specified braid implementing (14). Starting with the
ordered list, move \(i_1\) left to position one by consecutive rules
(13); then move \(i_2\) to position two, and \(i_3\) to position
three when present. In a swap \((X,Y)\mapsto(Y,YXY^{-1})\), the
right member moves left unchanged. Induction shows that the
selected matrices have become the first \(s\) entries unchanged
and in their original order. Therefore, for the resulting literal
finite braid operator \(\mathcal R_{\tau_I}\),
\[
 \mathcal O_I
    =\operatorname{Ad}_{\mathcal R_{\tau_I}}\Omega_{[s]}.
 \tag{15}
\]
Precisely, start with \(\mathcal U=I\) and, for each such row move
at position \(i\), update \(\mathcal U\leftarrow\mathcal U\mathcal R_i\).
Then \(\operatorname{Ad}_{\mathcal U}(H_j)\) is the updated list:
the new row formula is applied inside the existing conjugation.
This fixes the product order in \(\mathcal R_{\tau_I}=\mathcal U\).
There are \(\sum_{s=1}^3\binom ms\) observables, omitting empty
binomial coefficients. This is independent of \(N\).

Each \(\Omega_{[s]}\) commutes with the full ordered total generators:
its own block Casimir commutes with its block generators, and the
remaining coproduct factors commute with that block. Actual braid
intertwining therefore proves the same total invariance for
\(\mathcal O_I\). Equation (14) is an explicit bounded-degree
expression for this invariant, not just the definition by
conjugation with a growing matrix.

Indeed every entry of \(L_i^\pm\) and its inverse is a Laurent
polynomial in \(K_i\) and a polynomial in \(E_i,F_i\).
Equations (3),(14) give a finite expression with a degree bound
depending only on \(m\). Its coefficients are Laurent polynomials
in \(q\), with no inverse \(q-q^{-1}\). No original endpoint,
crossing scalar, or changed cut is needed to obtain (15).

## 3. The quotient also has bounded degree

Write \(x=-M/q\), \(f_n=\prod_{j=1}^n(1-Q^j)\).
R's actual quotient of any total intertwiner is
\[
 \mathcal B(O)=p_0S^{-1}Oi_0,\qquad
 S^{-1}=\sum_{n=0}^d
 \frac{(-1)^nQ^{n(n-1)/2}x^{-n}L_1^nF_{\rm r}^n}{f_n}.
 \tag{16}
\]
Here \(i_0\) inserts first occupation zero. The following bounded
formula in fact computes \(p_0S^{-1}Oi_0\) for any fixed Laurent
polynomial word \(O\), without an intertwining hypothesis.

Use (1) to order the first head as
\[
 O=\sum_{n,a,c}F_1^nK_1^aE_1^c\otimes O_{nac}.
 \tag{17}
\]
The finite sum has bounded indices depending only on the given
word degree. Commuting \(E_1\) past \(F_1\) introduces
\((q-q^{-1})(K_1-K_1^{-1})\), not its inverse.
Every term with \(c>0\) kills \(i_0\), and the other terms give
\(p_nOi_0=f_n\sum_a x^aO_{na0}\). Substitution in (16) cancels
the factorial exactly:
\[
 \boxed{\quad
 \mathcal B(O)=
 \sum_n(-1)^nQ^{n(n-1)/2}x^{-n}F_{\rm r}^n
                          \sum_a x^aO_{na0}.
 \quad}\tag{18}
\]
The remaining-head factors have their displayed order.
Terms \(n\ge N\) vanish on both sides: on the first head
\(F_1^N=0\), and on the remaining ordered tensor \(F_{\rm r}^N=0\).
The latter follows from the root Gaussian binomial formula.
Thus (18), with its fixed finite index set, applies at every level.
It neither divides by \(f_N\) nor expands the entire prefix matrix.

In particular all \(\mathcal B(\mathcal O_I)\) have Laurent degree
bounded independently of \(N\), with coefficients regular as \(q\to1\).
Their commutative leading expression is the substitution
\[
 E_1=0,\qquad K_1=x,\qquad F_1=-x^{-1}F_{\rm r}
 \tag{19}
\]
in the full observable. This is the actual \(F_\Sigma=0\) section,
since \(F_\Sigma=F_1+K_1^{-1}F_{\rm r}\). It gives
\(K_\Sigma=xK_{\rm r}\), \(E_\Sigma=E_{\rm r}\).
It is an observable calculation through the first vacuum, not a
generating-function or amplitude assertion for that vacuum.

## 4. Complete-root coherent symbols without missing arrows

This section concerns \(M=1\) only. On a finite head let
\(Xw_a=Q^aw_a\), and let \(S_0\) be the cyclic unit raising shift.
The actual matrices are exactly
\[
 E=S_0^{-1}(X^{-1}-1),\qquad
 F=S_0(1-QX),\qquad K=-q^{-1}X^{-1}.
 \tag{20}
\]
The putative bottom wrap of \(E\) has coefficient zero, as does
the top wrap of \(F\). Thus (20) is an equality of the original
nilpotent matrices, not a replacement by a different cyclic module.

Use the original binomial coherent kernel from J and divide it by
\((1+wz)^d\). A fixed word in (20) can be ordered as a finite sum
of \(S_0^sX^j\) with coefficient polynomials vanishing at every
input that would wrap. For \(N\) larger than its fixed degree,
its exact kernel is therefore a finite sum of
\[
 c_{sj}(q)\,w^s(1+Q^jwz)^d.
 \tag{21}
\]
To see the endpoint assertion, follow the word before ordering:
any path leaving the finite interval meets one of the two zero
coefficients in (20). Ordering gives the same matrix, so its
coefficient on a wrapping input is still zero. The usual binomial
sum then proves (21), with no unretained endpoint summand.

On a fixed compact complex chart with \(w\ne0\) and \(1+wz\ne0\),
put \(t=wz/(1+wz)\), \(c_0=2\pi i\). For bounded \(j\),
\[
 \left(\frac{1+Q^jwz}{1+wz}\right)^d
       =\exp(c_0jt)\bigl(1+O(N^{-1})\bigr).
 \tag{22}
\]
Taylor expansion of the logarithm proves this uniformly with
every fixed number of chart derivatives. Finite sums and tensor
products give the principal substitution
\[
 A=\exp(c_0t),\quad p=w^{-1},\qquad
 E=p(A^{-1}-1),\quad F=(1-A)/p,\quad K=-A^{-1}.
 \tag{23}
\]
It applies to the full and reduced observables above, including
their zeros, since no division by \(E\) or \(F\) was made.

Away from \(M=1\), the cyclic formula for \(E\) has an additional
endpoint row. It must be retained in meridian derivatives.
Equations (20)--(23) make no meridian-normal or whole-\(q\)-normal
claim. They are also not uniform symbol statements for a
degree-growing crossing, prefix star, or \(T\) kernel.

By M's Gauss reconstruction, (23) turns (3) into its actual ordered
classical \(SL_2\) meridians. The principal of (14) is precisely
\[
 o_I=\operatorname{tr}(H_{i_s}\cdots H_{i_1}).
 \tag{24}
\]
The conventional physical meridians are \(-H_i\); multiplying each
length-\(s\) trace by \((-1)^s\) is an explicit equivalent convention.

## 5. The finite trace family separates irreducible tuples

We prove this algebraically, including its local scheme meaning.
For \(A,B,C\in SL_2\), Cayley--Hamilton and trace give
\[
 AB+BA=(\operatorname{tr}A)B+(\operatorname{tr}B)A+
    \bigl(\operatorname{tr}(AB)-\operatorname{tr}A\operatorname{tr}B\bigr)I,
 \tag{25}
\]
\[
 \begin{split}
 \operatorname{tr}(ABC)+\operatorname{tr}(ACB)
 ={}&\operatorname{tr}(AB)\operatorname{tr}C+
 \operatorname{tr}(AC)\operatorname{tr}B+
 \operatorname{tr}(BC)\operatorname{tr}A\\
 &-\operatorname{tr}A\operatorname{tr}B\operatorname{tr}C.
 \end{split}\tag{26}
\]
For (25), apply the squared traceless-matrix identity to
\(A-\operatorname{tr}(A)I/2\) and \(B-\operatorname{tr}(B)I/2\).
Taking its product with \(C\) proves (26).
Together with cyclicity of ordinary trace, (26) recovers the
other orientation of every distinct triple from (24). Repeated
indices reduce by Cayley--Hamilton. Thus the one chosen order
in (14) supplies every trace of length at most three.

There are two explicit types of reconstruction charts.

First choose two generators \(A,B\), and write
\[
 a=\operatorname{tr}A,\quad b=\operatorname{tr}B,\quad
 c=\operatorname{tr}(AB),\qquad
 \Delta=a^2+b^2+c^2-abc-4.
 \tag{27}
\]
The trace Gram determinant of \(I,A,B,AB\) is \(-\Delta^2\).
Indeed for \(u=A-aI/2\), \(v=B-bI/2\), write
\(u^2=\alpha I\), \(v^2=\beta I\), \(uv+vu=\gamma I\).
Then \(\gamma^2-4\alpha\beta=\Delta\).
The basis \(I,u,v,uv-\gamma I/2\) has Gram determinant
\(2(4\alpha\beta-\gamma^2)(\Delta/2)=-\Delta^2\).
The change to \(I,A,B,AB\) has determinant one.
When \(\Delta\) is a unit these four matrices are a basis of
\(\operatorname{Mat}_2\). The traces against them recover the
coordinates of every \(H_j\) by this explicit Gram inverse.
They use only single, pair, and triple traces. The multiplication
table is fixed by \(A^2=aA-I\), \(B^2=bB-I\), and (25).

Second, choose three generators \(A,B,C\) for which
the trace Gram matrix of \(I,A,B,C\) is invertible.
Again pair traces recover all generator coordinates. Every
multiplication constant of this basis is recovered by taking
the traces of a product of two basis members against a third
and applying that Gram inverse. These are precisely traces of
length at most three, already supplied by (24),(26).

These finitely many charts cover every irreducible complex tuple.
Let \(L\) be the span of its traceless generator parts in
\(\mathfrak{sl}_2\). If \(\dim L=3\), the second chart applies.
If \(\dim L\le1\), all generators have a common eigenline.
If \(\dim L=2\) and the trace form on it is degenerate, its
radical contains a nonzero isotropic traceless matrix, hence a
nilpotent. Conjugate it to a nonzero multiple of \(e_{12}\).
Orthogonality forces the lower-left entry of every member of
\(L\) to vanish, again giving a common eigenline.
In the remaining two-dimensional case the trace form is
nondegenerate; any two generator parts forming a basis have
\(\Delta\ne0\), giving the first chart.
For a complete irreducible parabolic tuple one can simply choose
two distinct parabolic flags. Their nilpotent parts have nonzero
product trace, so (27) is nonzero.

Suppose two tuples on one of these charts have the same data
(24). The corresponding basis map preserves every multiplication
constant just computed. It is therefore an algebra isomorphism
between their full matrix algebras, sending every ordered
generator to its mate. This isomorphism is inner.
Here is also the local Artin-ring proof of that last assertion.
Let \(F_{ij}\) be the images of ordinary matrix units. Choose
\(v\) in the image of \(F_{11}\) lifting a nonzero vector of its
residue line, and put \(w=F_{21}v\). The relations of the \(F_{ij}\)
show that \((v,w)\) is a basis after reduction, hence over the
local ring. In this basis all \(F_{ij}\) are ordinary matrix
units. The change-of-basis determinant is a unit; a square root
of it exists locally over a complex Artin ring if an \(SL_2\)
representative is desired. Uniqueness is up to scalars, since a
matrix commuting with the full matrix algebra is scalar.

This proves equality of the local ordered-character relations,
not only a count of dimensions or separation of closed points.
The Gram denominators are the specified chart units. All
conjugations are one common conjugation of the whole tuple.

## 6. The actual opposite-kernel characteristic rows

Use J's actual operators, with all original scalars retained:
\[
 T=q_FE_\Sigma^d\mathscr C\,i_F(M^{-1}),\qquad
 J=H^{-1}T,\qquad H=D_N(MK_{\rm r}),
 \qquad K_0T=TK_0^{-1}.
 \tag{28}
\]
For each total-invariant \(\mathcal O_I\), define its literal
turned operator on the reflected space by
\[
 \mathcal O_I^\vee(M^{-1})
       =\mathscr C(M)^{-1}\mathcal O_I(M)\mathscr C(M).
 \tag{29}
\]
Turnover exchanges \(E,F\), inverts \(K\), and reverses the head
labels. Consequently (29) and its quotient also have the bounded
Laurent expressions just proved. The quotient descent and
commutation with \(E_\Sigma^d\) give the exact identities
\[
 \boxed{\quad
 \mathcal B(\mathcal O_I(M))T(M)
       =T(M)\mathcal B(\mathcal O_I^\vee(M^{-1})),\qquad
 \mathcal B(\mathcal O_I(M))J(M)
       =J(M)\mathcal B(\mathcal O_I^\vee(M^{-1})).
 \quad}\tag{30}
\]
For \(J\), use also that every \(\mathcal B(\mathcal O_I)\)
commutes with \(K_{\rm r}\), hence with \(H\).
These are finite actual source-compatible operator rows. They
do not require the kernel to have an asymptotic phase.

The whole normal row is also explicit. Set \(u=\log M\), write
\(A(u)=\mathcal B(\mathcal O_I(e^u))\), and let
\(A^\vee(v)\) be the quotient on the color-\(e^v\) module of the
turned word. Thus the right member of (30) is
\(J(u)A^\vee(-u)\). Turnover on the generators is exactly
\(E\leftrightarrow F,\ K\mapsto K^{-1}\), with reversed heads,
so this is one analytic bounded word, not an independently
chosen reflected symbol. Write
\[
 A(u)=A_0+uA_1+\cdots,\quad
 A^\vee(v)=A^\vee_0+vA^\vee_1+\cdots,\quad
 J(u)=\mathsf R/u+J_0+O(u).
 \tag{30a}
\]
J proves this simple-pole expansion. Comparing its two first
orders in (30) gives
\[
 A_0\mathsf R=\mathsf R A^\vee_0,\qquad
 A_0J_0-J_0A^\vee_0
       =-A_1\mathsf R-\mathsf R A^\vee_1.
 \tag{30b}
\]
These retain the original finite endpoint rows and scalar
normalizations. In particular the finite part \(J_0\) is not
asserted to intertwine the root observables by itself. Section 4
does not provide a principal symbol for the normal terms in
(30b).

Precisely, put \(T_0=T(1)\). Both actual root kernels
\(\mathcal K=T_0\) and \(\mathcal K=\mathsf R\) satisfy the
homogeneous rows
\[
 A_0\mathcal K=\mathcal K A^\vee_0,\qquad
 K_0\mathcal K=\mathcal K K_0^{-1}.
 \tag{30c}
\]
For \(T_0\) this is direct specialization of (30); for
\(\mathsf R\) it is the residue equation (30b).
If either of these sequences of root kernels has a regular
semiclassical characteristic relation on the coherent charts of
Section 4, its principal left and right actions, with the usual
dual input covector convention, impose
\[
 o_I(y)=o_I^\vee(z)\quad\hbox{for every }|I|\le3,\qquad
 k_{\rm r}(y)=k_{\rm r}(z)^{-1}.
 \tag{31}
\]
This assertion concerns \(T_0\) or \(\mathsf R\), not \(J_0\).
No homogeneous characteristic row for \(J_0\) follows without
controlling the two normal forcing terms in (30b). Nor is a
meromorphic phase across \(M=1\) asserted.
All principal functions in (31) were computed from
bounded operators in Sections 3--4. On the irreducible trace
charts of Section 5, its first equations identify the output
ordered tuple with the explicitly turned input tuple up to one
common conjugation. The oriented triple data remove the ambiguity
that interval traces alone could leave.

The label and frame transformation can be written explicitly.
At the complete classical point, let
\(J_{\rm mat}=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\).
Turnover has
\[
 (L_i^+)'=J_{\rm mat}(L_{m+1-i}^-)^{-1}J_{\rm mat},
 \qquad
 (L_i^-)'=J_{\rm mat}(L_{m+1-i}^+)^{-1}J_{\rm mat}.
 \tag{32}
\]
Put \(g=J_{\rm mat}B_m^-\), \(P=H_m\cdots H_1\). Multiplying
the ordered prefixes in (32) gives
\[
 g^{-1}H'_{m+1-j}g
 =(H_m\cdots H_{j+1})H_j(H_m\cdots H_{j+1})^{-1},
 \qquad P'=gPg^{-1}.
 \tag{33}
\]
For example before cancellation the first expression is
\(P P_{j-1}^{-1}H_jP_{j-1}P^{-1}\).
Equation (33) is the inverse-half-twist Hurwitz tuple. It retains
its explicit common conjugator, rather than declaring the
turned ordered tuple unchanged. The corresponding half-twist
presentation return identifies the underlying ordered character.

On the actual \(F_\Sigma=0\) section the total matrix \(P\) is
triangular and its selected first-axis eigenvalue is
\(K_\Sigma=xK_{\rm r}\). At completeness \(x=-1\). Thus the last
row of (31) changes this eigenvalue to its reciprocal.
If \(K_\Sigma^2\ne1\), the two total-product eigenlines are
distinct; the row selects the opposite eigenline, after the
explicit character identification (33). Turnover by itself
transports the original eigenline with its old eigenvalue into
the \(E_\Sigma=0\) polarization; the additional row in (31) is
what distinguishes the other \(F_\Sigma=0\) choice.

This conclusion is on the local augmented character quotient.
The common frame, its residual moment constraint, the actual
half-twist, and all relative source windows remain. No pointwise
map of the original integration chains is inferred. In particular
the relative-window defect specified in J is not set to zero.

## 7. Scope and complete proof directs

The new result is the explicit finite quantum separator (14)--(15),
the bounded quotient formula (18), and the homogeneous root rows
(30c). Their local characteristic equations (31), when defined,
have the ordered-character and reciprocal-flag interpretation above.
The trace-chart proof works over local Artin rings. The uniform
coherent-symbol calculation is only at \(M=1\); the finite part
\(J_0\) retains its exact normal forcing.

It does not prove that \(T\) or \(J\) has a nonzero Fourier-integral
amplitude on that relation, that any geometric branch occurs in
the original cycle, or that short-tangle and complementary-source
contributions cannot cancel. Meridian and quantum normals retain
their complete original endpoint rows and scalar lines.

* M: notes/marked_braid_holonomy.md,
  SHA256 eff47c757d0e44bda0c396c094315b8e1fce11f1fc2d6445d636c6d2d3a46c4f.
* Q: notes/regular_holonomy_braiding.md,
  SHA256 5be349365f59c89d4e20ce411a93baa850562056b62b13ad4d465b1b1607f9ef.
* R: notes/research_actual_reduced_braid_source.md,
  SHA256 9a472ef27b08305a519ff1f24b6d2b909e63a0acbdc49b3a29e001c52a2f2243.
* J: notes/research_opposite_polarization_source_kernel.md,
  SHA256 d52c6dd8e62f575a262fc7af460e258f7cb0e40b5a9c037ac46dd8d151002d44.

All four complete directs were read nontruncated in the active
author sequence. Only written mathematics and text/hash operations
were used. Frozen and public files were not edited.
