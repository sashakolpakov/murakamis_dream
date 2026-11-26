# Reciprocal lowering flags and the actual root radical

Private written proof, 19 November 2026. Author-final for independent review.

The reciprocal Cartan-pair image of the actual prefix reduction is
exactly the endomorphism algebra of a two-periodic exact lowering
complex. This identifies its admissibility condition with explicit
physical flags. Together with the original first-normal source
order, it proves that the Jacobson radical of the entire actual
root intertwiner algebra has cube zero, uniformly in the level and
width. Only the units congruent to one modulo this radical form the
resulting two-step nilpotent group.

The complete directs are P, the first-jet source order, and C, the
actual prefix Ward equations. The lowering-chain, division-free
Ward, flag, and radical arguments are proved below. This is a
statement about the full Cartan-preserving source algebra. Its
integer-degree-preserving subalgebra is retained where a braid word
requires it, but no separate classification of that subalgebra is
asserted.

## 1. The actual pair and the image already determined by the source

Fix
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,
 \quad m=r+1\ge2,
 \qquad M=1,\quad x=-q^{-1}.
 \tag{1}
\]
Let \(U\) be the tensor of the remaining \(r\) physical heads,
with actual totals \(E,F,K\). The total operators on all \(m\)
heads are denoted by a subscript \(\Sigma\). Set
\[
 K^N=\varepsilon I,\qquad \varepsilon=(-1)^{(N+1)r},
 \qquad \mathcal A=\operatorname{End}_K(U).
 \tag{2}
\]
Each actual weight space \(U_\chi\) has dimension
\(D=N^{r-1}\). The weight set is closed under inversion.

For an actual total intertwiner \(W\), C gives
\[
 W'=S^{-1}WS=\sum_{n=0}^{d}F_1^n\otimes B_n,
 \qquad KB_n=Q^nB_nK,
 \tag{3}
\]
and the literal transformed lowering operator
\[
 E'=S^{-1}E_\Sigma S=I\otimes E+L_1b_A,
 \qquad b_a=KQ^{-a}-K^{-1}.
 \tag{4}
\]
The second term vanishes at first occupation zero. All terms have
the physical cap. In particular \([E',W']=0\).

Let \(V\subset\mathcal A\) be the set of root matrices \(B_0\)
arising from these actual intertwiners. P proves that every root
intertwiner has an analytic meridian lift and identifies the full
root algebra with
\[
 \mathcal T=V\oplus(\mathcal A/V),\qquad
 (b,[c])(b',[c'])=(bb',[bc'+cb']).
 \tag{5}
\]
Here the first and second components are the value and first
\(\mu=\Log M\) coefficient of the actual reduced family. The
normal-layer ideal in (5) is square-zero.

For a nonself reciprocal pair \(\mathfrak o=\{\chi,\chi^{-1}\}\),
P supplies its central projector in \(V\) and proves
\[
 \dim V_{\mathfrak o}=D^2,\qquad
 V_{\mathfrak o}=V_{\mathfrak o}^{\perp_\beta},
 \quad
 \beta((X,Y),(X',Y'))=a_\chi\operatorname{Tr}(XX'-YY'),
 \quad a_\chi=\frac{\chi-\chi^{-1}}{2\varepsilon m}.
 \tag{6}
\]
On a self weight \(\chi=\pm1\), P proves that \(V\) is the
entire matrix block and that its normal quotient is zero.

Since \(\chi^{2N}=1\), for a nonself pair there is a unique
\(s\in\{1,\ldots,d\}\) such that \(Q^s=\chi^2\). The two
actual lowering maps of interest are
\[
 A=E^s:U_{\chi^{-1}}\longrightarrow U_\chi,
 \qquad B=E^{N-s}:U_\chi\longrightarrow U_{\chi^{-1}}.
 \tag{7}
\]
Their directions follow from \(KE=QEK\). No power of \(F\)
or extra Cartan factor is included in (7).

## 2. Full physical lowering chains

The operator \(E\) on \(U\) has only Jordan chains of length
\(N\). This follows directly from the actual tensor structure.
For one head, its coefficients
\[
 e_a=Q^{-a}-1,\quad 1\le a\le d,
 \tag{8}
\]
are nonzero, and its two outward arrows are zero. For more heads,
split the first remaining head from the rest, writing
\[
 E=E_{\rm h}K_{\rm t}+E_{\rm t}.
 \tag{9}
\]
The two summands \(Q\)-commute. The finite quantum binomial
identity at primitive \(Q\) therefore gives inductively
\(E^N=E_{\rm h}^NK_{\rm t}^N+E_{\rm t}^N=0\). This uses
the actual zero endpoint arrows.

For \(0\le b\le d\), consider
\[
                E^b(w_d\otimes v),\qquad v\in U_{\rm t}.
 \tag{10}
\]
Their least first-head occupation is \(d-b\), with coefficient
\((e_d\cdots e_{d-b+1})K_{\rm t}^b\). This is a unit. The
joint map in (10) is consequently triangular and invertible.
It provides \(N^{r-1}\) independent length-\(N\) chains, since
applying \(E\) advances the displayed power and the next power
after \(d\) is zero. Choosing \(v\) in a Cartan weight space
makes each chain homogeneous. Each chain contains each of the
\(N\) actual Cartan weights once.

It follows on each chain, and hence on the actual weight spaces,
that
\[
 AB=BA=0,\qquad \operatorname{im}A=\ker B,
 \qquad \operatorname{im}B=\ker A.
 \tag{11}
\]
Indeed the two weights in (7) occur at distinct positions in one
linear chain. Exactly one of the two indicated forward paths
stays inside that chain; the other crosses its zero endpoint.

Write \(k=\operatorname{rank}A\), \(l=\operatorname{rank}B\).
Then \(k+l=D\). For \(r\ge2\) these ranks are explicitly
\[
                 k=(N-s)N^{r-2},\qquad l=sN^{r-2}.
 \tag{12}
\]
To count them, the starting weights of (10) are
\(xQ^{-d}\kappa\), with \(\kappa\) a rest weight. Every rest
weight occurs \(N^{r-2}\) times. Thus the position of
\(\chi^{-1}\) is uniformly distributed among the \(N\)
positions of these chains; exactly \(N-s\) positions permit
\(s\) further steps. For \(r=1\), \(D=1\): if
\(\chi^{-1}=xQ^{-a}\), then \(k=1\) precisely when
\(a\ge s\); otherwise \(k=0\), and always \(l=1-k\).

## 3. The division-free Ward constraint

We prove that the actual root image commutes with both arrows of
(7). This step does not invert any resonant coefficient \(b_a\).

Let \(i_n v=w_n\otimes v\), and restrict the full prefix
space to total weight \(x\lambda\). Its \(n\)-th first-head
component has tail weight \(Q^n\lambda\). For
\(0\le n\le t<N\), direct expansion of (4) gives
\[
 p_0(E')^t i_n\big|_{U_{Q^n\lambda}}
       =c_{t,n}(\lambda)E^{t-n},
 \quad
 c_{t,n}(\lambda)=Q^{n(n-1)/2}{t\brack n}_Q
              \prod_{j=t}^{t+n-1}(\lambda-Q^{-j}\lambda^{-1}).
 \tag{13}
\]
For \(n=0\) the coefficient is one, and for \(n>t\) the
left side is zero. To verify the formula including all orders,
separate the first step in (4). The term that keeps the first
occupation and the term that lowers it give respectively
\[
 c_{t,n}(\lambda)
 =c_{t-1,n}(Q\lambda)
       +(\lambda-Q^{-n}\lambda^{-1})c_{t-1,n-1}(Q\lambda).
 \tag{14}
\]
The initial coefficient is \(c_{0,0}=1\). Substituting (13)
in (14) reduces it to the two finite Pascal identities for
\({t\brack n}_Q\). This proves (13) inductively. All Gaussian
coefficients have index less than \(N\); no denominator
\(1-Q^N\) occurs.

If \(\lambda^2=Q^{-t}\), every coefficient in (13) with
\(n\ge1\) vanishes because its product contains
\(\lambda-Q^{-t}\lambda^{-1}\). Thus on this actual total
weight space
\[
                       p_0(E')^t=E^t p_0.
 \tag{15}
\]
Also \((E')^t i_0=i_0E^t\) without any weight restriction.
Apply \(p_0\) to \((E')^tW'i_0=W'(E')^t i_0\), and use
(3) and (15). It follows that
\[
        E^t B_0|_{U_\lambda}=B_0|_{U_{Q^t\lambda}}E^t.
 \tag{16}
\]
Take \((\lambda,t)=(\chi^{-1},s)\) and then
\((\chi,N-s)\). For \((X,Y)=(B_0|_{U_\chi},
B_0|_{U_{\chi^{-1}}})\), this proves
\[
                         XA=AY,\qquad YB=BX.
 \tag{17}
\]
Every intermediate physical first-head term was retained before
the common factor made it zero. In particular (17) was not
obtained by formally dividing C's scalar Ward recurrence at a
root resonance.

## 4. Exact flag classification and the first-normal quotient

Choose complements in the exact complex (11):
\[
 U_\chi=P\oplus Q_*,\qquad P=\operatorname{im}A=\ker B,
 \qquad
 U_{\chi^{-1}}=R_*\oplus T_*,\qquad
 R_*=\operatorname{im}B=\ker A.
 \tag{18}
\]
The dimensions are \((k,l)\) and \((l,k)\), respectively.
Use \(A:T_*\to P\) and \(B:Q_*\to R_*\) to identify
the complementary coordinates. Solving (17) now gives exactly
\[
 \boxed{\qquad
 X=\begin{pmatrix}a&b\\0&d_*\end{pmatrix},\qquad
 Y=\begin{pmatrix}d_*&f\\0&a\end{pmatrix}.
 \qquad}\tag{19}
\]
Here \(a\in\operatorname{Mat}_k\),
\(d_*\in\operatorname{Mat}_l\),
\(b\in\operatorname{Mat}_{k\times l}\), and
\(f\in\operatorname{Mat}_{l\times k}\) are arbitrary.
For example \(XA=AY\) kills the lower-left block of \(X\)
and identifies its \(a\) with the lower-right block of \(Y\);
the other arrow does the complementary job.

The algebra in (19) has dimension
\(k^2+l^2+2kl=D^2\). Equation (17) includes
\(V_{\mathfrak o}\) in this algebra, while P gives precisely
that dimension in (6). Therefore
\[
 \boxed{\qquad
 V_{\mathfrak o}=\operatorname{End}(U_{\chi^{-1}}
                  \mathop{\rightleftarrows}^{A}_{B}U_\chi).
 \qquad}\tag{20}
\]
The intrinsic statement is preservation of the two physical flags
and compatibility with both arrows. The complements in (18) only
display its matrix form.

Its ideal \(J\) consisting of the two off-diagonal blocks
\((b,f)\) satisfies \(J^2=0\), and
\[
           V_{\mathfrak o}/J
                 =\operatorname{Mat}_k\oplus\operatorname{Mat}_l.
 \tag{21}
\]
A zero-size matrix factor is omitted. Thus \(J\) is its
Jacobson radical: a nilpotent ideal is contained in that radical
by the finite geometric-series inverse, and the displayed matrix
quotient has zero radical. The latter is elementary: for a
nonzero matrix \(T\), a suitable rank-one \(S\) makes \(I-ST\)
singular, excluding \(T\) from the radical criterion.

The same flags explicitly describe the quotient normal layer in
(5). If a representative of \(\mathcal A_{\mathfrak o}/
V_{\mathfrak o}\) has blocks \((C,D_*)\) in (18), its
class is determined by
\[
 C_{11}-(D_*)_{22},\quad C_{22}-(D_*)_{11},\quad
                         C_{21},\quad(D_*)_{21}.
 \tag{22}
\]
The two upper-right blocks disappear in the quotient. Pairing
with (19) is exactly
\[
 a_\chi\bigl[
 \operatorname{Tr}_k((C_{11}-(D_*)_{22})a)
 +\operatorname{Tr}_l((C_{22}-(D_*)_{11})d_*)
 +\operatorname{Tr}_l(C_{21}b)-\operatorname{Tr}_k((D_*)_{21}f)
 \bigr].
 \tag{23}
\]
Thus (6) identifies this quotient with \(V_{\mathfrak o}^*\),
including its actual scalar \(a_\chi\). This is a bimodule
identification. If \(\phi_c(v)=\beta(c,v)\), cyclicity and
the central coefficient of \(\beta\) give
\[
          (b\phi_c)(v)=\phi_c(vb),\qquad
                       (\phi_c b)(v)=\phi_c(bv),
 \tag{24}
\]
exactly the actions inherited from multiplication in
\(\mathcal A/V\). It is not a Hermitian duality.

## 5. Cube-zero radical of the whole actual root algebra

On a nonself pair, (5) and (24) identify the entire actual root
factor with the trivial extension
\[
 T(V_{\mathfrak o})=V_{\mathfrak o}\oplus V_{\mathfrak o}^*,
 \qquad (b,\phi)(b',\phi')=(bb',b\phi'+\phi b').
 \tag{25}
\]
Define
\[
                       \mathfrak r_{\mathfrak o}
                             =J\oplus V_{\mathfrak o}^*.
 \tag{26}
\]
This is an ideal. Its quotient is (21). Its cube is zero:
a product containing two dual factors is zero, as is a product
with two adjacent \(J\) factors. The only other possible
three-factor product is \(j\phi j'\). For every \(v\in V\),
\[
                       (j\phi j')(v)=\phi(j'vj)=0,
 \tag{27}
\]
because \(J\) is an ideal and \(J^2=0\). Hence
\[
                    \mathfrak r_{\mathfrak o}^{3}=0.
 \tag{28}
\]
The nilpotent-ideal and matrix-quotient argument following (21)
shows that (26) is the entire Jacobson radical, not merely a
nilpotent subideal.

The central pair projectors from P split (5): they are central
in the ambient \(\mathcal A\) and therefore also in its
quotient bimodule. Each self-Cartan factor has no normal quotient
and is the full semisimple matrix algebra. Consequently, if
\(\mathfrak R\) is the Jacobson radical of the actual full root
intertwiner algebra on all \(m\) heads, then
\[
                       \boxed{\quad\mathfrak R^3=0.\quad}
 \tag{29}
\]
The bound does not depend on \(N\) or \(m\). For one remaining
head, every nonself pair has \(k=0\) or \(l=0\), so \(J=0\)
and that factor's radical already has square zero. The assertion
(29) concerns the full Cartan commutant. It does not claim that
passing to an arbitrary subalgebra preserves this radical
classification or these rank formulas.

## 6. Finite radical transport and the original source

The radical unit group \(1+\mathfrak R\) has nilpotence class at most two.
For \(X,Y\in\mathfrak R\),
\[
 (1+X)^{-1}=1-X+X^2,
 \quad
 (1+X)(1+Y)(1+X)^{-1}(1+Y)^{-1}=1+[X,Y],
 \tag{30}
\]
and the last commutator is central within \(1+\mathfrak R\).
Equivalently,
\[
 e^X=1+X+\tfrac12X^2,\quad
 \log(1+X)=X-\tfrac12X^2,\quad
 \log(e^Xe^Y)=X+Y+\tfrac12[X,Y].
 \tag{31}
\]
These follow by expansion and (29). For any element \(T\) of
the actual root algebra, its conjugation is also exact at second
order:
\[
                  e^XTe^{-X}=T+[X,T]+\tfrac12[X,[X,T]].
 \tag{32}
\]
Every omitted term has three radical factors, with ordinary
algebra factors between them, and vanishes because
\(\mathfrak R\) is an ideal and \(\mathfrak R^3=0\).
The full unit group contains the nonnilpotent matrix groups of
(21); it has not been declared nilpotent.

All these coordinates keep the original source. P's exact
formula for a root class \((b,[c])\) is
\[
 \Phi_0(b,[c])=\operatorname{Tr}(d_0b)
                         +\operatorname{Tr}(d_{-1}c),
 \quad
 d_0=\frac{K+K^{-1}}{2\varepsilon},\qquad
 d_{-1}=\frac{K-K^{-1}}{2\varepsilon m}.
 \tag{33}
\]
On the pair in (19), this becomes
\[
 \frac{\chi+\chi^{-1}}{\varepsilon}
                           (\operatorname{Tr}a+\operatorname{Tr}d_*)
 +a_\chi\bigl[
    \operatorname{Tr}_k(C_{11}-(D_*)_{22})
       +\operatorname{Tr}_l(C_{22}-(D_*)_{11})\bigr].
 \tag{34}
\]
In particular the normal layer is not discarded by the flag
classification. Crossings and
framing scalars included in an actual word remain in its two
jet coefficients; any prescribed outside scalar retains its
own product-rule derivatives.

The theorem gives explicit physical flags for admissibility and
uniform algebraic nilpotence in the actual finite source. It
does not estimate the condition numbers of the chosen flag
complements, identify these Cartan pairs with selected geometric
eigenflags, or prove positivity or nonvanishing of the closing of
a prescribed braid. No geometric Regge or framing group is
identified with the radical unit group.

## Complete direct-source pins

* P: notes/research_prefix_first_jet_source_order.md, 434 lines,
  SHA256 ffdf484ab0222b99dc937b24ef940af91070609e4e85cf8675e20a500eb53ad5.
* C: notes/research_prefix_commutant_and_pointed_normal_functional.md,
  549 lines, SHA256
  b4fb801a1482316aebb4799f1d0b80d5b43ced39138d903c04cfde811ca166b0.

The complete matching P read from the immediately preceding formal
review is retained fresh and unchanged in this author sequence.
The complete C was freshly read nontruncated in covering chunks.
The entire matching final was freshly read back nontruncated, every
used implication checked, and all three pins renewed before freezing.
Independent matching review and parent adoption remain separate.
Only written mathematics and text/hash operations were used. Frozen
and public files were unchanged.
