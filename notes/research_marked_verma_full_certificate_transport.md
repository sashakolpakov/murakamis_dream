# The full highest-cut certificate transports to marked Verma moments

Private written proof, 18 November 2026.

The original highest-cut finite array admits a full certificate with no
internal multiplication variables. This note keeps independent index
weights through its root specialization, ordinary-color restriction and
canonical completion at \(q=1\). It obtains an exact triangular system
for every bounded collection of polynomial index moments. The endpoints,
ordinary pivots and zero-framing scalar remain those of the original word.

The diagonal operator is a specified coefficient of that full certificate.
It is not replaced by an arbitrary scalar right factor. No assertion is
made that this diagonal has the regular two-branch node required by the
canonical cutoff analysis, or that the inserted Borel germs have already
been continued through that node.

## 1. Fixed source, coordinates and marked periods

Fix a \(b\)-strand braid \(\beta\) whose permutation is one cycle. Let
\(w\) be its writhe and set
\[
 Q=q^2,\qquad c=b-1-w.
\tag{1}
\]
The parity of the braid permutation gives \(c\in2\mathbb Z\). Keep the
highest input and output index zero on the cut strand and the original
zero-framing convention. Use the actual signed crossing coefficients
of [F, (2)], with their common Cartan factor removed.

All strand-matching equations, including the two fixed cut indices, are
homogeneous integral linear equations independent of the color and the
root level. Choose once an integral basis \(k=(k_1,\ldots,k_s)\) of their
solution lattice. Each physical label and transfer is an integral linear
function of \(k\). Conversely each \(k_i\) is an integral linear function
of the physical labels: the kernel of a map between free abelian groups
is a direct summand, since its quotient is the free image of that map.
Thus this coordinate choice needs no level-dependent translation.

Let \(I_N(q,x;k)\) be [C]'s entire off-root summand, including its
pivot and framing, extended by zero outside its actual finite support.
For independent units \(\mathbf w=(w_1,\ldots,w_s)\), retain
\[
 F_N(q,x;\mathbf w)=\sum_k\mathbf w^k I_N(q,x;k).
\tag{2}
\]
At fixed \(N\) this is a finite Laurent polynomial in the \(w_i\).
Negative coordinate values cause no difficulty. The weights are
independent of \(N\) and of the external meridian shift.

For a positive integral color \(L\), let \(C_{L,\mathbf w}(q)\) be the
same weighted finite-color highest-cut word, with ordinary pivots and
ordinary zero framing. It is a specified array evaluation, generally
not an invariant under changing the braid presentation. At
\(\mathbf w=1\) it is the original reduced scalar \(C_L(q)\).

## 2. The whole certificate and its exact root restriction

[C, Sections 3--5] supplies a nonzero finite operator
\[
 P(q,x,z,T,\mathbf S)I_N=0,\qquad
 z=q^N,\quad Tf(x)=f(qx),\quad S_iI(k)=I(k+e_i),
\tag{3}
\]
whose coefficients contain no internal multiplication characters.
The equality is pointwise on the zero-extended array, including every
boundary stratum. Its coefficients can be taken Laurent-polynomial in
\(x,z\), with rational \(q\)-coefficients.

Remove the maximal common factor \((z+1)^a\) from the coefficients of
the entire operator. This division is legitimate before any root
specialization: at each fixed \(N\), \(q^N+1\) is a nonzero rational
function of generic \(q\), and hence may be canceled in the pointwise
identity (3). Call the quotient \(P^\circ\). Then
\[
 \overline P(q,x,T,\mathbf S)
       =P^\circ(q,x,-1,T,\mathbf S)\ne0.
\tag{4}
\]
The finite entries, including all shifted entries, are regular at
\(q_N=e^{\pi i/N}\) for generic \(x\): their factorial indices are
less than \(N\), and their zero extensions introduce no denominators.
Excluding the finitely many levels at which fixed rational
\(q\)-coefficients have poles, (4) annihilates the actual root array.
No factor of an individual specialized term has been canceled.

Summation with the weights in (2) gives exactly
\[
 \overline P(q_N,x,T,\mathbf w^{-1})F_N(q_N,x;\mathbf w)=0.
\tag{5}
\]
Indeed translating a zero-extended finite sum replaces \(S_i\) by
\(w_i^{-1}\). This operation retains, rather than omits, its endpoint
terms.

Now fix \(L\ge1\) and put \(x=q_N^{L-1}\), with \(N>L\). The positive
and negative products in [F, (2)] vanish whenever a high strand index
would decrease across \(L\). For the positive sign the obstructing
factor is \(1-x^{-2}Q^{L-1}\); for the negative sign it is
\(1-x^2Q^{1-L}\). A high index therefore propagates along its physical
strand. Since the closure has one component, it would eventually reach
the fixed cut index zero. Consequently every contributing label is
less than \(L\), exactly as in [F, Section 4]. Multiplying a term by
\(\mathbf w^k\) changes no zero and no index transition.

These are the same local entries as [C]'s checked crossings on every
supported label. Substituting [C]'s displayed \(E^n\) product and
\(\frac{[a]_q!}{[n]_q![a-n]_q!}=q^{-n(a-n)}{a\brack n}_Q\) into its two
finite series gives respectively the two expressions [F, (2)].
For the inverse series the two factors \((-1)^n\) cancel, and its
remaining \(q\)-power cancels before the factor \(Q^{-ab'}\).
Thus the use of the signed high-index barriers involves no change
of local frame or a new sign convention.

The framing comparison is also exact. At the root the \(b-1\) auxiliary
pivots and the residual writhe factor in [C] give
\[
 x^{-c(N-1)}Q^{-\sum a_i},
\]
whereas the ordinary-color source of [F] has
\(x^cQ^{-\sum a_i}\). Their ratio at this color is
\[
 x^{-Nc}=q_N^{-Nc(L-1)}=(-1)^{c(L-1)}=1.
\tag{6}
\]
This includes negative writhe. Under an external shift \(T^j\), replace
\(L\) by \(L+j\); (6) remains one. If the operator has inverse shifts,
choose \(L\) larger than their fixed negative range and \(N\) larger
than every shifted positive color. Thus
\[
 F_N(q_N,q_N^{L+j-1};\mathbf w)
                =C_{L+j,\mathbf w}(q_N)
\tag{7}
\]
for every shift occurring in (5), with exactly the same coordinate
weights. The common Cartan factors have already been removed in both
sources; their zero-framing corrections are precisely those used in
(6). There is no quantum-dimension division at the cut.

For fixed \(L\), the expression obtained from (5) using (7) is a finite
Laurent polynomial in \(\mathbf w\), with rational \(q\)-coefficients.
It vanishes at infinitely many distinct \(q_N\). Each coefficient is
therefore identically zero. We have proved the generic-color identity
\[
 \left.
 \overline P(q,x,T,\mathbf w^{-1})C_{L,\mathbf w}(q)
 \right|_{x=q^{L-1}}=0
\tag{8}
\]
for every sufficiently large integral \(L\), where \(T^j\) on the
source means color \(L+j\). This is an identity of the actual weighted
finite sources, not an inference from their unweighted scalarity.

## 3. The canonical marked completion at \(q=1\)

Write \(\delta=1-Q\). On the untruncated basis use [F, (2)] and the
same marked word. Its graded highest-cut trace is
\[
 V_\beta(Q,x;\tau,\mathbf w)
 =x^c\sum_{a_2,\ldots,a_b\ge0}
       \tau^{\sum a_i}Q^{-\sum a_i}
       \sum_{\text{internal paths}}\mathbf w^k
       \langle0,\mathbf a|B_\beta|0,\mathbf a\rangle_{\rm path}.
\tag{9}
\]
Each fixed total-index sector is finite. Expressing \(k\) in physical
labels writes the weight as a product of diagonal marks at fixed word
stages. Transfer labels are differences of adjacent strand labels, so
they introduce no different kind of insertion.

At \(Q=1\), every crossing is the linear substitution of [F, (4)].
Each mark is a diagonal linear substitution. Let
\(L_\beta(x,\mathbf w)\) be their literal ordered product and put
\[
 T_0=\operatorname{diag}(0,1,\ldots,1),\qquad
 D_\beta(x,\tau,\mathbf w)
       =\det(I-\tau L_\beta(x,\mathbf w)T_0).
\tag{10}
\]
No inverse of \(T_0\) is taken. The coefficient proof in
[F, Sections 2--3] applies with these marks retained: the normal-order
\(j\) word is a finite sum of degree-zero differential operators of
order at most \(2j\), followed by the marked linear substitution.
Conjugation through the invertible diagonal marks preserves that order.
The determinant trace argument therefore gives
\[
 [\delta^j]V_\beta
  \in \frac{\mathbb Q[x^{\pm1},\mathbf w^{\pm1},\tau]}
               {D_\beta(x,\tau,\mathbf w)^{2j+1}}.
\tag{11}
\]
As in [F], temporary meridian denominators cancel coefficientwise in
\(\tau\), since every original sector coefficient is Laurent in
\(x,\mathbf w\). Only the stated determinant denominator remains.

At \(x=1\), the two signed crossing matrices swap their variables.
The marked word is consequently a diagonal-weighted permutation with
one cycle. Deleting the cut input column breaks that cycle, so
\[
 (L_\beta(1,\mathbf w)T_0)^b=0,\qquad
 D_\beta(1,\tau,\mathbf w)=1.
\tag{12}
\]
In particular every fixed meridian derivative of (11) at \(x=1\)
is polynomial in \(\tau\). This is the marked regularity needed for
ordinary-color restriction; it is not assumed from the unmarked case.

Define, coefficientwise in \(\delta\),
\[
 \mathcal W_\beta(\delta,Y;\mathbf w)
 =V_\beta\left(1-\delta,
             \sqrt{Y/(1-\delta)};1,\mathbf w\right).
\tag{13}
\]
The staggered sign conjugation in [F, Section 4] commutes with every
diagonal mark, and \(c\) is even. Thus (13) is independent of the
square-root choice. Its coefficients are rational in \(Y,\mathbf w\)
and regular near \((Y,\mathbf w)=(1,1)\).

The high-index argument above also applies before root specialization
on \(x=q^{L-1}\). Equation (12) permits evaluation at \(\tau=1\) after
each formal coefficient is taken. Hence the exact formal restrictions
are
\[
 \mathcal W_\beta(\delta,(1-\delta)^L;\mathbf w)
       =C_{L,\mathbf w}((1-\delta)^{1/2}).
\tag{14}
\]
In particular the construction is canonical for this fixed marked
word and coordinate choice. No presentation independence is asserted
away from \(\mathbf w=1\).

Set \(h=\log Q\), so \(q=e^{h/2}\), and let
\(\mathsf T f(Y)=f(e^hY)\). Transport (8) by the exact substitution
\(x=\sqrt{Ye^{-h}}\). Clear the common coefficient denominators of
the whole operator; this also removes any coefficient pole at \(h=0\).
Its left side on (13) is formal and regular near
\((h,Y,\mathbf w)=(0,1,1)\). Put \(u=\log Y\). Every homogeneous
degree in \((h,u)\), restricted to \(u=Lh\), is a polynomial in
\(L\), with formal coefficients in \(\mathbf w-1\). Equations (14)
and (8) make it zero for all sufficiently large \(L\). The polynomial
is zero. Thus the whole marked identity is
\[
 \mathscr P(h,Y,\mathsf T,\mathbf w^{-1})
           \mathcal W_\beta(1-e^h,Y;\mathbf w)=0.
\tag{15}
\]
The transported operator is nonzero: the substitutions in its
coefficients and commuting internal variables are injective, and its
formal shift monomials remain distinct. A local square-root branch
near \(Y=1\) is enough for its coefficients; no coefficient evenness
is required. Each normal coefficient of (15) is an algebraic meridian
identity (rational after adjoining that square root), and therefore
continues coefficientwise away from its specified poles. This proves
transport of the full marked certificate, not just its scalar member.

## 4. An exact triangular system for polynomial moments

Expand the nonzero transported certificate at internal shifts one:
\[
 \mathscr P=\sum_\beta A_\beta(h,Y,\mathsf T)(\mathbf S-1)^\beta,
 \qquad h_0=\min_{A_\beta\ne0}|\beta|.
\tag{16}
\]
Choose \(\alpha\) lexicographically least among its nonzero degree-
\(h_0\) terms. Let
\[
 \mathcal F(\mathbf t)=\mathcal W_\beta(1-e^h,Y;e^{\mathbf t})
       =\sum_\gamma M_\gamma(h,Y)\frac{\mathbf t^\gamma}{\gamma!},
 \qquad
 \mathscr P(e^{-\mathbf t})=\sum_\nu C_\nu\mathbf t^\nu.
\tag{17}
\]
Here \(M_\gamma\) is exactly the original index coupon \(k^\gamma\).
We have \(C_\nu=0\) for \(|\nu|<h_0\), and
\(C_\nu=(-1)^{h_0}A_\nu\) at degree \(h_0\).
Taking the coefficient of \(\mathbf t^{\alpha+\gamma}\) in (15) gives
\[
 A_\alpha M_\gamma
 =(-1)^{h_0+1}\gamma!
   \sum_{\substack{\nu\le\alpha+\gamma\\\nu\ne\alpha}}
       C_\nu\,
       \frac{M_{\alpha+\gamma-\nu}}{(\alpha+\gamma-\nu)!}.
\tag{18}
\]
Every nonzero term on the right is earlier in graded lexicographic
order. If \(|\nu|>h_0\), its moment degree is smaller than
\(|\gamma|\). If \(|\nu|=h_0\), a nonzero term has
\(\nu>\alpha\) lexicographically, so
\(\alpha+\gamma-\nu<\gamma\). For any fixed \(d\), (18) is therefore
a finite triangular system on \(|\gamma|\le d\), with the same
diagonal operator \(A_\alpha\). The zero-dimensional and \(h_0=0\)
cases obey the same formula. Negative external shifts have already
been included in (8), and no new division is made in (18).

There is also an exact clock specialization. For fixed integral
\(m\in\mathbb Z^s\), substitute \(\mathbf t=hm\) into (15):
\[
 \mathscr P(h,Y,\mathsf T,e^{-hm})
       \mathcal W_\beta(1-e^h,Y;e^{hm})=0.
\tag{19}
\]
This keeps the full coupon \(Q^{m\cdot k}\). It is not obtained by
discarding high polynomial moments when \(k\) is of order \(1/h\).

## 5. Exact scope of the new transport

The identities are formal quantum-normal identities of the actual
marked source. Its moments have rational meridian coefficients; the
transported operator may use the chosen square-root coordinate.
They neither assert convergence of its \(h\)-series nor provide joint
Borel continuation in the coupon parameters. A fixed moment can be
taken in (18); a full clock germ must retain (19).

In particular \(A_\alpha M_0=0\), but a scalar right divisor of
\(A_\alpha\) need not act diagonally on the other moments. Nothing here
proves that this lexicographic coefficient has a regular transverse
abelian/nonabelian node, or a cofactor invertible at the node of a
different supplied scalar operator. That source-compatible local
reduction and the resulting inserted cutoff estimates remain unpaid.
The theorem supplies the actual marked equations on which such a
reduction can work. It does not identify a geometric character or
give a scalar lower bound.

The proof uses the following complete texts, read in full with the
used implications checked:

| Label | Complete direct source | SHA256 |
|---|---|---|
| C | notes/finite_sum_annihilator.md | d6e973b5f43049d7e68b35bd32b6677871815c240c97e74b2a6bed3e00370ae3 |
| F | notes/research_classical_verma_rational_loops.md | f88f5fc4d1eb0f68f9270e581bd0e1bfd43c669cef989d9813f6000feb4e3659 |

Only written mathematics and source-text reads were used. No mathematical
programs, tests or builds were run. Frozen sources and public documents
are unchanged.
