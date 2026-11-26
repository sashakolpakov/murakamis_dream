# Uniform physical bounds for rational-word Casimir transport

Written proof, 24 November 2026.

Every fixed original rational word transports the two pair-Casimir
observables to operators with uniformly bounded norm in the original
physical Hilbert--Schmidt metric. The bound is independent of the
quantum level. Commutators of any fixed pair of these transported
observables are \(O(N^{-1})\) in that same metric.

The new estimate uses a finite cyclic-Weyl representation on the
actual four-index arrays, with the physical endpoint factors retained.
The exact Fricke identities and their rational-word transport are
already proved in [B]. Their role here is to propagate a new uniform
physical norm estimate, rather than to assert a new operator algebra.

As a consequence, any sublinear selected family of full generalized
eigenspaces of a transported Casimir has a subexponentially conditioned
physical frame. No norm bound for the rational word or its inverse,
and no lower bound for its original scalar closing, is inferred.
An additional application compares low-degree polynomial observations
of an actual transported coherent packet with that same packet in
the physical metric. Its finite extraction method is already in [O].

## 1. Original packet space and observables

Let \(N\ge3\), \(d=N-1\), \(q=e^{\pi i/N}\), \(Q=q^2\),
\(x=q^d=-q^{-1}\), and \(c_0=q+q^{-1}\).
Use the full original Hopf-box algebra and its physical metric from [P]:
\[
 \mathcal A_N=\mathbb C[\Omega]\simeq
       \mathbb C[Z]/P_N(Z),\qquad
 P_N(Z)=2T_N(Z/2)+2,\qquad
 \|B\|_{\rm ph}^2=\operatorname{Tr}(B^*B).
 \tag{1}
\]
Here \(T_N\) is the Chebyshev polynomial of the first kind.
The basis \(w_0,\ldots,w_d\) on each physical head is orthonormal.
The physical quarter-turn is the genuine unscaled turn \(T\), not
the swap of the two heads. For a complete physical Hopf box it is
\[
 (TB)_{a,b;c,e}=x^{a-e}B_{d-a,c;b,d-e}.
 \tag{2}
\]
It preserves \(\mathcal A_N\), is unitary in (1), and satisfies
\(T^2=I\). All original cup/cap and pivot factors in (2) remain.

Write \(L_f(B)=fB\) for multiplication in the actual algebra, and set
\[
 X=L_\Omega,\qquad Y=TXT,\qquad
 \mathsf R=L_{R_N},\qquad
 \kappa=q^{d^2/2}.
 \tag{3}
\]
Here \(R_N\) is the original positive crossing polynomial, including
its Cartan scalar \(\kappa\). Its inverse is its full Hermite inverse,
not an inverse defined only on distinct eigenvalues. In particular
\(\mathsf R\) and \(T\) are invertible on the full space (1).

A fixed rational word \(W_N\) is a fixed finite composition of \(T\)
and \(\mathsf R^{\pm1}\). Fixed integer twist powers can equivalently
be used as generators. The word and its integer powers are fixed
before \(N\) varies. Any recorded scalar framing unit remains in
the word; it cancels when an observable is conjugated.

**Theorem 1.** Define \(Z\) in (15) below. For every fixed word \(W\),
the actual transported operators
\[
 X_W=W_NXW_N^{-1},\quad
 Y_W=W_NYW_N^{-1},\quad
 Z_W=W_NZW_N^{-1}
 \tag{4}
\]
satisfy
\[
       \max(\|X_W\|_{\rm ph},\|Y_W\|_{\rm ph},\|Z_W\|_{\rm ph})
                                      \le C_W.
 \tag{5}
\]
The norm is the operator norm on the packet space (1). For any two
fixed words \(W,V\) and any \(A_W\in\{X_W,Y_W,Z_W\}\),
\(B_V\in\{X_V,Y_V,Z_V\}\),
\[
                         \|[A_W,B_V]\|_{\rm ph}\le C_{W,V}/N.
 \tag{6}
\]
Constants may depend on the fixed words, but not on \(N\).
No assertion in (5) bounds \(\|W_N\|\) or \(\|W_N^{-1}\|\).

## 2. Literal ambient formulas and the boundary wraps

For the estimate, embed (1) in the full four-index Hilbert space
\(\mathscr B_N=\operatorname{End}(V_N\otimes V_N)\).
Write an array as \(B(a,b;c,e)\), with every index in
\(\{0,\ldots,d\}\). The same expression (2) defines a unitary
involution \(\widetilde T\) on this whole Hilbert space: its index
permutation is an involution, and its two successive phases are
\(x^{a-e}\) and \(x^{e-a}\). Its restriction to the original
Hopf boxes is precisely \(T\). No different boundary invariant is
defined by using this linear extension for a norm estimate.

Let \(\widetilde X(B)=\Omega B\) and
\(\widetilde Y=\widetilde T\widetilde X\widetilde T\).
Direct substitution of the original balanced generators in [P] gives
\[
 \begin{split}
 (\widetilde XB)(a,b;c,e)={}&D_X(a,b)B(a,b;c,e)\\
 &+A_+(a,b)B(a+1,b-1;c,e)\\
 &+A_-(a,b)B(a-1,b+1;c,e),
 \end{split}
 \tag{7}
\]
where
\[
 \begin{split}
 D_X(a,b)&=2q^{-1}Q^{-b}+2qQ^a-(q+q^{-1})Q^{a-b},\\
 A_+(a,b)&=Q^{-b}(1-Q^b)(1-Q^{a+1}),\\
 A_-(a,b)&=Q^{-b-1}(1-Q^{b+1})(1-Q^a).
 \end{split}
 \tag{8}
\]
Only existing physical indices are used in (7). For example the
\(A_+\) term is zero if \(a=d\) or \(b=0\), and the \(A_-\)
term is zero if \(a=0\) or \(b=d\). These are exact root zeros.

Conjugating (7) by the literal formula (2) gives
\[
 \begin{split}
 (\widetilde YB)(a,b;c,e)={}&D_Y(a,c)B(a,b;c,e)\\
 &+B_-(a,c)B(a-1,b;c-1,e)\\
 &+B_+(a,c)B(a+1,b;c+1,e),
 \end{split}
 \tag{9}
\]
with
\[
 \begin{split}
 D_Y(a,c)&=2q^{-1}(Q^{-a}+Q^{-c})
                          -(q+q^{-1})Q^{-a-c-1},\\
 B_-(a,c)&=q^{-1}(1-Q^{-a})(1-Q^{-c}),\\
 B_+(a,c)&=q(1-Q^{-a-1})(1-Q^{-c-1}).
 \end{split}
 \tag{10}
\]
For clarity, before simplification its lower-shift coefficient is
\(xQ^{-c}(1-Q^c)(1-Q^{-a})\), and its upper-shift coefficient is
\(x^{-1}Q^{-c-1}(1-Q^{c+1})(1-Q^{-a-1})\).
These follow from the phases \(x\) and \(x^{-1}\) introduced by
the two corresponding turns. They simplify to (10) using
\(x=-q^{-1}\).

The \(B_-\) term vanishes if \(a=0\) or \(c=0\), while the
\(B_+\) term vanishes if \(a=d\) or \(c=d\). Therefore (7),(9)
can now be read with all indices taken cyclically modulo \(N\):
every newly introduced wrap term has coefficient zero. This check
is needed even at even levels, where \(x^N=-1\). We have not
assumed that the turn phase itself is an ordinary \(Q\)-clock.
The exact zero factors remove its possible wrap discrepancy.

## 3. Finite cyclic-Weyl estimates in the physical metric

On the cyclic array indices \(r=(a,b,c,e)\), define
\[
 (M_\alpha B)(r)=Q^{\alpha\cdot r}B(r),\qquad
 (S_vB)(r)=B(r+v\bmod N),\qquad
 \alpha,v\in\mathbb Z^4.
 \tag{11}
\]
Both are unitary in the ambient physical Hilbert--Schmidt metric.
Expanding the factors in (8),(10) expresses
\(\widetilde X,\widetilde Y\) as fixed finite sums of monomials
\(M_\alpha S_v\), with exponents bounded independently of \(N\)
and uniformly bounded scalar coefficients.

The exact multiplication rule is
\[
 (M_\alpha S_v)(M_\beta S_w)
       =Q^{\beta\cdot v}M_{\alpha+\beta}S_{v+w}.
 \tag{12}
\]
Thus the commutator of two such monomials has norm at most
\(|\beta\cdot v-\alpha\cdot w|\,|Q-1|\).
Summing the fixed number of terms proves
\[
 \|[\widetilde X,\widetilde Y]\|
                         \le C|Q-1|\le C'/N.
 \tag{13}
\]
Restriction gives the same estimate for the original \(X,Y\).
Also [P] and unitarity of the turn give
\[
                         \|X\|,\|Y\|\le18.
 \tag{14}
\]
No exponentially conditioned change from Newton coordinates was used.

For \(N\ge3\), put \(\Delta=q^2-q^{-2}\) and define the original
Fricke-conjugated operator
\[
 Z=\frac8{c_0}I+\frac{q^{-1}YX-qXY}{\Delta}.
 \tag{15}
\]
This is not a new definition of a source transform: [B] proves that
it equals the actual \(D_1\) on the full original Hermite algebra.
Its apparent small denominator has a bounded physical numerator.
Indeed
\[
 q^{-1}YX-qXY=q^{-1}[Y,X]+(q^{-1}-q)XY,
 \tag{16}
\]
and \(c_0\ge1\), \(|\Delta|^{-1}\le N/4\) for \(N\ge3\).
Equations (13),(14) already give a level-independent norm for \(Z\).

We need a little more than its norm. The same quotient has a finite
cyclic-Weyl extension of fixed complexity with bounded coefficients.
Pair one term of \(\widetilde Y\widetilde X\) with its reversed
term in \(\widetilde X\widetilde Y\). Apart from their common
bounded scalar, the quotient coefficient is
\[
 \frac{q^{-1}Q^a-qQ^b}{q^2-q^{-2}}
   =\frac{q^2Q^b}{c_0}
                 \frac{Q^{a-b-1}-1}{Q-1},
 \qquad a,b\in\mathbb Z\text{ fixed}.
 \tag{17}
\]
The last ratio is a finite Laurent sum with at most
\(|a-b-1|\) terms, or zero. Its coefficients have modulus one.
This proves the assertion also when distinct monomial labels
coincide modulo a small level. The scalar \(8/c_0\) is bounded.
The extension is used only to estimate the actual restriction (15).

More generally, any two fixed noncommutative polynomial expressions
in \(X,Y,Z\), with fixed Laurent polynomials in \(q\) as scalar
coefficients, admit such finite cyclic-Weyl extensions. Their
physical norms are bounded, and their commutator is \(O(N^{-1})\)
by (12). The fixed expressions may have different degrees; their
constants are allowed to depend on those expressions.

## 4. Exact generator closure for every fixed rational word

The required algebra identities are prior exact source results, not
principal-symbol replacements. In the full Newton basis [A,B], let
\(C=X\), \(J=Y\), and
\[
 V_n=\kappa^nT\mathsf R^{-n}T,\qquad
 D_n=V_nXV_{-n}.
 \tag{18}
\]
The signed Fricke identities in [B] give \(D_1=Z\) and
\(T D_{-1}T=Z\). Consequently
\[
                         \mathsf RY\mathsf R^{-1}=Z.
 \tag{19}
\]
The divisor-free recurrence [B, equation (17a)] is
\[
                  qD_{n+2}+q^{-1}D_n+D_{n+1}Y=8I,
                    \qquad n\in\mathbb Z.
 \tag{20}
\]
Set \(G_n=T D_{-n}T=\mathsf R^nY\mathsf R^{-n}\).
Conjugating (20), with its index reversed, gives
\[
                G_{n+2}=8qI-q^2G_n-qG_{n+1}X,
 \quad G_0=Y,\quad G_1=Z.
 \tag{21}
\]
In particular define
\(Z_-=8q^{-1}I-q^{-2}Z-q^{-1}YX\).
The exact conjugation rules are
\[
 \begin{array}{c|ccc}
  &X&Y&Z\\ \hline
 \mathsf R(\cdot)\mathsf R^{-1}
   &X&Z&8qI-q^2Y-qZX\\
 \mathsf R^{-1}(\cdot)\mathsf R
   &X&Z_-&Y\\
 T(\cdot)T&Y&X&Z_-
 \end{array}
 \tag{22}
\]
The order of every product is part of these identities.
For the last entry, \(TZT=\mathsf R^{-1}Y\mathsf R=G_{-1}\)
follows from \(Z=D_1\), and (21) gives precisely \(Z_-\).
All crossing and turn normalizations are those in (3),(18).

Repeated substitution in (22) writes every operator (4) as a fixed
noncommutative polynomial in \(X,Y,Z\), with scalar coefficients
that are Laurent polynomials in \(q\). Its degree and
number of terms may depend on the fixed word. Section 3 therefore
proves both (5) and (6). This is an exact root-level transport of
the full operators, including every first-normal direction.

The algebra identities in [B] already retain those normals and prove
the divisor-free recursion. That note obtains
\(\|D_n\|\le C_nN^{4|n|}\) in the ordinary canonical-polynomial
real norm. The later [O, section 2] already proves uniform fixed-word
observable bounds in the Newton coefficient norm. The estimate here
is uniform in the original physical Hilbert--Schmidt operator norm,
by the finite-Weyl realization. No equivalence between those packet
metrics, and no transport of a Newton adjoint into this metric, is assumed.

## 5. Moving full-cluster frames

There is a quantitative consequence for the actual transported
invariant spaces. Fix a word \(W\), and put
\(A_W=W_NXW_N^{-1}\) on \(\mathcal A_N\).
Similarity preserves its full minimal polynomial \(P_N\).
Its generalized eigenspaces are exactly
\[
       \mathcal S_{W,j}=W_N\mathcal A_{N,j},
 \tag{23}
\]
where \(\mathcal A_{N,j}\) is the original primary ideal.
Their dimensions remain the original multiplicities one or two.
Choose a physical Hilbert--Schmidt orthonormal basis \(E_{W,j}\)
inside each selected full generalized eigenspace, and concatenate
any \(m\) distinct nodes into \(E_W\).

The derivative-zero cardinal proof in [C] applies without requiring
that \(A_W\) be normal or complex symmetric. The cosine-node gaps
are unchanged, and (5) gives
\(\|A_W-c_jI\|\le C_W+2\).
For clarity, use selected multiplicities \(\nu_j\in\{1,2\}\) and
\[
 \ell_j(z)=\prod_{k\ne j}
                \left(\frac{z-c_k}{c_j-c_k}\right)^{\nu_k}.
 \tag{24}
\]
Take \(h_j=\ell_j\) at a simple node and
\(h_j=(1-\ell_j'(c_j)(z-c_j))\ell_j\) at a double node.
Then \(h_j(A_W)E_{W,k}=\delta_{jk}E_{W,k}\) exactly.
The same factorial denominator as [C] yields
\[
 \|h_j(A_W)\|
       \le\exp\{C_W[m\log(eN/m)+\log N]\}.
 \tag{25}
\]
This evaluates the actual operator factors and does not replace a
nonnormal operator norm by the supremum on its scalar spectrum.
Recover each coefficient block by \(h_j(A_W)\), sum their squared
norms, and use the triangle inequality for the upper bound. Thus
\[
 \boxed{\quad
 e^{-C_W\Lambda_{N,m}}I\le E_W^*E_W\le mI,
 \qquad \Lambda_{N,m}=m\log(eN/m)+\log N .
 \quad}
 \tag{26}
\]
Every selected block is complete, including its actual transported
normal direction. For any \(m_N=o(N)\), (26) controls arbitrary
coherent coefficient vectors with subexponential cost.

There is no assertion of a polynomial adapter from specified raw
vectors \(W_Nv\) to these internally orthonormal blocks. In
particular (26) does not normalize the actual source, bound its
transport amplitude, or control the ambient spectral projection.
The filters only recover blocks on the selected invariant sum;
their values on unselected blocks have not been set to zero.

## 6. An actual coherent-source observation theorem

Here the same physical bounds have a direct application to full
source packets. We restate the generating unit and extraction
identities from [O]; the new assertion is their consequence in the
physical metric, not a new extraction method.

For \(v_j=qQ^j\), define
\[
 \mathcal D_j(t)=\prod_{r=-j+1}^{0}(1+q^{-1}Q^rt),\qquad
 \mathcal B_j(t)=\prod_{r=j+2}^{N-j}(1+q^{-1}Q^rt).
\]
The actual centered generating unit \(A_N(t,\zeta)\), canonical of
degree less than \(N\) in \(\zeta\), is specified by its full jets:
\[
 \begin{split}
 A_N(t,c_j)&=\mathcal D_j(t)^2\mathcal B_j(t),\\
 \partial_\zeta A_N(t,c_j)
   &=\frac{\mathcal D_j(t)^2t\,\partial_t\mathcal B_j(t)}
                       {v_j-v_j^{-1}}
                    \quad\hbox{at double nodes}.
 \end{split}
 \tag{27}
\]
The canonical indices are \(0\le j\le\lfloor d/2\rfloor\).
At the odd simple middle only the value is prescribed. All products
use the original empty-product convention. These are the actual
generating-unit jets in [O], including their first-normal normalization.
They determine \(A_N\) uniquely, with \(A_N(0,\zeta)=1\).
In particular it is a unit for \(|t|<1\), since all its displayed
node factors are nonzero there.

Retain the original coherent source packet
\[
 \mathcal F_N(t)=N^{-1/2}R_N A_N(t,\zeta),\qquad
 w_N(y,z)=\mathcal F_N(y)\mathcal F_N(z)
        =N^{-1}R_N^2A_N(y,\zeta)A_N(z,\zeta).
 \tag{28}
\]
Its scalar \(N^{-1}\) is not changed by our metric choice.
Write \(M_t=L_{A_N(t)}\), \(M_w=L_{w_N(y,z)}\), and
\(\mathcal L_n=\mathsf R^{-n}Y\mathsf R^n\).
The norm-free full-Hermite gauge identity [O, equation (10)] is
\[
 b_t(X)M_t\mathcal L_nM_t^{-1}
       =\mathcal L_n-c_0t\mathcal L_{n+1}
                         +t^2\mathcal L_{n+2}+8tI,\qquad
 b_t(X)=I+tX+t^2I.
 \tag{29}
\]
That identity retains the seam zeros and the coalescing first
normals before it is asserted in the quotient. It is not a relation
in the distinct-root value quotient alone.

Set \(B_w=M_wYM_w^{-1}\). Apply (29) twice and retain the exact
\(R_N^2\) in (28). As [O] proves, \(b_y(X)b_z(X)B_w\) is a finite
combination of \(X,I,\mathcal L_{-2},\ldots,\mathcal L_2\) with
coefficients polynomial in \(y,z,q,q^{-1}\). Theorem 1 bounds
their conjugates by any fixed \(W\) in the physical metric.
Choose \(0<\rho_W<1\) with
\(\rho_W C_W+\rho_W^2\le1/2\). A Neumann series gives
\(\|b_t(X_W)^{-1}\|\le2\) for \(|t|\le\rho_W\).
Consequently
\[
 \|WXW^{-1}\|_{\rm ph}+
           \|WB_wW^{-1}\|_{\rm ph}\le K_W,
       \qquad |y|,|z|\le\rho_W ,
 \tag{30}
\]
uniformly in \(N\). No separate norm bound for \(M_t\), \(M_w\),
or their inverses is used.

The other input is the exact finite-head extractor of [O].
For \(1\le D\le N/32\) and a nonzero polynomial \(P\) of degree
at most \(D\), it constructs a noncommutative polynomial
\(\mathscr A_{P,N}\) with
\[
 \mathscr A_{P,N}(X,Y)P(X)1=1,\quad
 \deg\mathscr A_{P,N}\le5D,\quad
 \|\mathscr A_{P,N}\|_{\rm coeff,1}
       \le\frac{e^{CD}(N/D)^{12D}}{\|P\|_2}.
 \tag{31}
\]
Here \(\|P\|_2\) is its ordinary monomial coefficient norm.
To specify the extractor, [O] uses the monic source kernel rows
\(g_j=K_j/\ell_j\), where
\(K_j(\zeta)=\sum_{r=0}^j e_r(c_j)e_r(\zeta)\),
\(e_r(\zeta)=S_r^{-2}\prod_{a<r}(c_a-\zeta)\), and
\(\ell_j=(-1)^jS_{2j}/S_j^4\).
Their lowering coefficients are
\(\beta_j=s_j^8/(s_{2j-1}s_{2j}^2s_{2j+1})>0\), with
\(s_j=2\sin(\pi j/N)\), \(S_j=\prod_{r=1}^j s_r\).
On the head \(g_0,\ldots,g_{2D}\), let
\(F_j(Y)=\prod_{0\le r\le2D,\ r\ne j}(Y-c_r)/(c_j-c_r)\).
Expand \(P=\sum_{j\le D}a_jg_j\), choose the index supplied by [O],
and take
\[
 \mathscr A_{P,N}
       =\frac{F_0(Y)X^jF_j(Y)}
                         {a_j\prod_{r=1}^j\beta_r}.
\]
The sole descending path gives (31). The two factorially bounded
filters and its descending coefficient give the exponent \(12D\).
This is an identity in the full algebra; its proof in a finite
polynomial head does not erase any physical normal after conjugation.

**Theorem 2.** For every fixed word there are \(C_W,N_0\) such that,
for \(N\ge N_0\), \(1\le D\le N/32\), \(\deg P\le D\), and
\(|y|,|z|\le\rho_W\),
\[
 \boxed{\begin{split}
 &e^{-C_WD}(D/N)^{24D}\|P\|_2^2\|Ww_N\|_{\rm ph}^2\\
 &\hspace{8mm}\le\|WP(X)w_N\|_{\rm ph}^2
       \le e^{C_WD}\|P\|_2^2\|Ww_N\|_{\rm ph}^2 .
 \end{split}}
 \tag{32}
\]
For \(D=0\), the exact identity is
\(\|WP(X)w_N\|_{\rm ph}^2=|P|^2\|Ww_N\|_{\rm ph}^2\).
The zero polynomial is included trivially.

To prove the lower bound, conjugate (31) by the actual invertible
\(\mathcal U=WM_w\). Its two generators become \(X_W\) and
\(WB_wW^{-1}\), bounded by (30). Its coefficient sum and degree
therefore bound the conjugated extractor by
\(e^{C_WD}(N/D)^{12D}/\|P\|_2\). It maps \(WP(X)w_N\) exactly to
\(Ww_N\). The resulting norm inequality, squared, proves the lower
bound. The upper bound follows from
\(WP(X)w_N=P(X_W)Ww_N\) and (5).
The physical value \(\|1\|_{\rm ph}=N\) has not been set to one;
it appears in neither ratio because extraction compares these same
two transported packets.

If \(D_N=o(N)\) and \(\|P_N^{\rm obs}\|_2=1\), (32) implies
\[
 \frac1N\log
  \frac{\|WP_N^{\rm obs}(X)w_N(y,z)\|_{\rm ph}^2}
       {\|Ww_N(y,z)\|_{\rm ph}^2}\longrightarrow0
       \qquad(|y|,|z|\le\rho_W)
 \tag{33}
\]
uniformly on that bidisc. The unit \(w_N\) and invertible word make
the denominator nonzero. The new physical rate of \(Ww_N\) is
not computed here and need not equal its untransported rate.
Nor does (33) bound the original marked scalar from below.

There is also an exact specialization to the original empty packet.
At \(y=z=0\), use (32) with the fixed word
\(V=W\mathsf R^{-2}\). Since \(w_N(0,0)=N^{-1}R_N^2\)
and \(P(X)\) commutes with \(\mathsf R\), its two packets become
\(N^{-1}WP(X)1\) and \(N^{-1}W1\). Hence (32), and the
sublinear-degree conclusion (33), hold with \(w_N\) replaced by
\(1\), with constants depending on \(W\).

## 7. Source and geometric scope

The construction always uses the genuine physical quarter-turn,
the original positive crossing polynomial and its full inverse,
and the complete algebra (1). It makes no replacement of the
original marked cap, pivot, framing, or external normalization.
Its four-index extension is a norm-estimating realization of these
same operators, not a changed state sum.

Uniformly bounded conjugated observables do not imply that \(W_N\)
or its inverse has subexponential norm. They also do not imply a
lower bound for a selected coefficient or for the original closing
of \(W_N(1)\). No geometric canonical graph or contributing cycle
is identified solely from the finite-Weyl symbols.

An arbitrary Conway product of two independent child packets is
not an invertible rational-word conjugacy. Its actual mixed forcing,
described in [B], is not removed by (22). Turns or changes to
overlapping pairings may move a chosen cluster, and its exterior
and original closing still require their own source estimates.
No new knot-volume lower bound or finite-exception theorem is
claimed here.

## Complete inputs and closest coverage

All five complete texts were read at their matching versions.

| Label | Complete text | SHA256 |
| --- | --- | --- |
| P | [Uniform physical Conway source](research_conway_uniform_physical_quartic.md), 477 lines | 39895b430535f565d30133b46ef57f67589207bc83f40597ffe96e2ce79bbda8 |
| B | [Exact finite-band unit-turn and branching operator](research_unit_turn_finite_band_branching_operator.md), 730 lines | 31d9f574c7dc3aaac07e4eb50c131b3328be46b3c2a2ef46f9dae7f0c4ddb9cb |
| A | [Actual Newton turn and original signed alphabet](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/actual_newton_turn_positive_gram.md), 434 lines | d8b21fa8db909120035e86e997a0e02cb84f8dce2dcf6fb244bb5c85c17e28a3 |
| C | [Selected physical Casimir-cluster Gram](research_sublinear_physical_casimir_cluster_gram.md), 412 lines | 7cfecc06fdba21757a89abd8e33d630aaccf6a306de1fd6f4f35bbedce6dabdb |
| O | [Coherent observations through fixed words](research_short_word_coherent_observation_transport.md), 509 lines | ff2fbaaa56c48bc6845bd58f964e10de66483df550a4b30005aed244ff0a0398 |

Only written mathematics, complete text reads, and metadata hashes
were used. No mathematical program, numerical experiment, test,
build, earlier-final edit, or public-manuscript change was made.
