# Whole endpoint-coupon folding with the original normal channels

Private written proof, 16 November 2026.

The shared endpoint coupons in the full-period vertical-current formula
can be reduced together, before estimating the surviving source. Their
value part has only half the original frequency band, independently of
the number of cut incidences. The remainder is an explicit original
normal functional, with polynomial coefficient norm. Applying this
construction to the whole charged coupon puts every affected vertex's
remaining traced charge in a fixed upper-half lattice interval, even if
its input charge was outside that interval. The physical-evaluation terms retain every
surviving edge and every joint spectator.

This is a finite source identity and a polynomial-cost reduction. It
does not bound the resulting coherent partially evaluated sources by a
classical face action. In particular, a radical term is retained rather
than declared zero, and neighboring physical evaluations do not delete
the kernel between them.

## 1. Physical data and the exact Chebyshev fold

Use
\[
 N\ge2,\quad D=N-1,\quad m=\lfloor N/2\rfloor,\quad
 J=D-m=\lfloor(N-1)/2\rfloor,\quad \eta=(-1)^D,\quad\theta=\pi/N,
\]
\[
 P_N(z)=2T_N(z/2)+2,\qquad
 \mathcal A_N=\mathbb C[z]/(P_N),\qquad
 \phi_N(f)=\eta N^2[z^D]\operatorname{rem}_{P_N}f,
 \tag{1}
\]
and the original Newton polynomials and kernel
\[
 s_j=2\sin(j\theta),\quad S_j=\prod_{b=1}^j s_b,\quad S_0=1,
 \quad c_a=2\cos((2a+1)\theta),
\]
\[
 e_j(z)=S_j^{-2}\prod_{b<j}(c_b-z),\qquad
 K_N(w,z)=\sum_{j=0}^D e_j(w)e_j(z).
 \tag{2}
\]
There are double nodes \(c_a\), \(0\le a<m\), and additionally the
simple node \(c_J=-2\) when \(N\) is odd. Their positive angular lifts are
\[
 c_a=-2\cos\tau_a,\qquad \tau_a=\pi(D-2a)/N>0.
 \tag{3}
\]
The full original trace is
\[
 \phi_N(f)=\eta\sum_{a<m}
       \{(4-c_a^2)f'(c_a)-c_af(c_a)\}
              +\mathbf1_{N\ {\rm odd}}f(-2).
 \tag{4}
\]
Thus equality of all these values and first normals is equality in
\(\mathcal A_N\). The radical \(\mathfrak r_N\) consists of classes
vanishing at every distinct node and satisfies \(\mathfrak r_N^2=0\).
The full-high source proves (4) and this assertion; the endpoint source
also supplies the odd simple term and the \(N=2\) normalization.

Put \(x=-z/2\), so \(T_N(x)=\eta\) in \(\mathcal A_N\), and define
\[
             \mathcal R_N(x)=(1-x^2)U_{N-1}(x).
             \tag{5}
\]
The cosine addition identities give, in the full quotient,
\[
 \boxed{\quad
 T_{N-k}(x)=\eta T_k(x)+\mathcal R_N(x)U_{k-1}(x),\qquad
 T_{N+k}(x)=\eta T_k(x)-\mathcal R_N(x)U_{k-1}(x).
 \quad}                                                    \tag{6}
\]
Here \(0\le k\le N\) suffices, and \(U_{-1}=0\). Before taking the
quotient, replace \(\eta\) in (6) by \(T_N(x)\). Also
\[
 \mathcal R_N^2=(1-x^2)(1-T_N(x)^2)=0
                       \quad\hbox{in }\mathcal A_N.          \tag{7}
\]
These folds retain the normal difference between the two frequencies.

Indeed, at \(z=-2\cos t\),
\[
 \mathcal R_N=\sin t\sin Nt,\qquad
 \mathcal R_N(c_a)=0,\qquad
 \mathcal R_N'(c_a)=\eta N/2.                                \tag{8}
\]
It also vanishes at the odd simple node. Formula (8) follows by
differentiating in \(t\) and dividing by \(dz/dt=2\sin t\).
Its nonzero normal at every double node shows that it generates
\(\mathfrak r_N\) as an ideal. Equations (4) and (8) give the exact
normal-channel identity
\[
 \phi_N\bigl(\mathcal R_N U_{k-1}(x)f\bigr)
        =2N\sum_{a<m}\sin\tau_a\sin(k\tau_a)f(c_a).            \tag{9}
\]
In particular its coefficient norm is at most \(N^2\), for integral
\(k\), but the functional need not vanish. If \(N=2m\), (6) at \(k=m\)
reads \(2T_m=\mathcal R_NU_{m-1}\): the midpoint frequency is itself
radical. This is why the value band stops at \(J=m-1\) at even levels.
At odd levels the degree-\(m\) value polynomial is retained, including
its value at the simple node.

## 2. Bounds for a shared microscopic endpoint product

Fix \(0<\alpha_0<\pi\). At one surviving vertex let
\[
 0\le h_i\le\alpha_0/N,\quad w_i=2\cosh h_i,\quad
 B_i(z)=K_N(w_i,z),\quad Q(z)=\prod_{i=1}^r B_i(z),           \tag{10}
\]
where the number \(r\) of cut incidences is fixed but arbitrary.
The empty product is one. Constants below may depend on \(r,\alpha_0\),
but not on \(N\) or these heights.

Write the exact ordinary split
\[
 B_i=L_i+R_i,\quad
 L_i(z)=\sum_{j=0}^J e_j(w_i)e_j(z),\quad
 R_i(z)=\sum_{r'=0}^{m-1}e_{D-r'}(w_i)e_{D-r'}(z).           \tag{11}
\]
At the distinct physical nodes,
\[
 B_i(c_a)=L_i(c_a)=F_{a,N}(w_i),\qquad
                F_{a,N}(w)=K_N(c_a,w).                     \tag{12}
\]
The endpoint theorem proves that the zeros of \(F_{a,N}\) are greater
than \(2\), its value at \(c_0\) is one, and consequently
\[
       |F_{a,N}(w)|\le1\quad\hbox{if }|w-2|\le2-c_0.
                                                               \tag{13}
\]
For all sufficiently large \(N\), the entire range (10) lies in this
disk: \(\cosh(\alpha_0/N)+\cos(\pi/N)<2\). Therefore
\[
           |B_i(c_a)|\le1,\qquad |Q(c_a)|\le1               \tag{14}
\]
uniformly at all distinct nodes. These are modulus bounds; positivity
for \(h_i>0\) is not required. The finitely many smaller levels give
bounded compact families and will be absorbed in constants.

We also need a uniform bound on the high coefficients in (11).
Directly from (2),
\[
 |e_j(2)|=\prod_{b<j}
       \left(\frac{\sin((b+1/2)\theta)}
                        {\sin((b+1)\theta)}\right)^2
                       \le1\quad(0\le j\le D).             \tag{15}
\]
To check the inequality, the sign of
\(\sin((b+1)\theta)-\sin((b+1/2)\theta)\) changes at most once,
from positive to negative. Hence the successive products decrease
and then increase, and their maximum is at one of the two endpoints.
Those endpoint values are \(1\) and
\[
             |e_D(2)|=\frac1{N^2\sin^2(\pi/(2N))}\le1.
                                                               \tag{16}
\]
The half-sine product gives the equality in (16), also recorded in
the current source. For \(\delta=w_i-2\ge0\), the logarithmic
derivative of \(P_N\), with multiplicities retained, yields
\[
 \sum_{a=0}^{N-1}\frac1{2-c_a}
       =\frac{P_N'(2)}{P_N(2)}=\frac{N^2}{4}.
\]
It follows that
\[
 |e_j(w_i)|\le
 \exp(\delta N^2/4)
 \le\exp\{\alpha_0^2\cosh(\alpha_0/2)/4\}=:E_{\alpha_0}.
                                                               \tag{17}
\]
This bound holds at every level, for every index \(j\le D\).

Let \(P_Q\) be the unique polynomial of degree at most \(J\) with
\(P_Q(c_a)=Q(c_a)\) at every distinct physical node. Then exactly
\[
             [Q]=[P_Q]+\Delta_Q,\qquad\Delta_Q\in\mathfrak r_N.
                                                               \tag{18}
\]
For a degree-\(J\) polynomial \(P\) whose nodal modulus is at most \(M\),
the folded \(N\)-point cosine orthogonality in the endpoint source gives
\[
 P(z)=\sum_{k=0}^J a_kT_k(-z/2),\qquad
       |a_0|\le M,\quad |a_k|\le2M\ (k>0).
                                                               \tag{19}
\]
The odd endpoint has weight \(1/N\), while every paired node has
weight \(2/N\); no endpoint is omitted. In particular, for \(P_Q\),
\[
                    \sum_{k=0}^J|a_k|\le C_{\alpha_0,r}N.   \tag{20}
\]
For sufficiently large \(N\), the constant in (20) can be one.

**Lemma 1 (full normal bound).** Set
\[
             \gamma_a=\eta(4-c_a^2)(Q'-P_Q')(c_a).
                                                               \tag{21}
\]
At every level and all heights (10),
\[
                      \sum_{a<m}|\gamma_a|
                              \le C_{\alpha_0,r}N^3.       \tag{22}
\]
For every spectator \(f\), with arbitrary additional variables,
\[
                \phi_N(\Delta_Q f)=\sum_{a<m}\gamma_a f(c_a).
                                                               \tag{23}
\]

**Proof.** Formula (23) is (4): the value of \(\Delta_Q\) vanishes,
so the derivative of \(f\) and the odd simple term vanish.
For any polynomial as in (19), the Chebyshev derivative formula gives
\[
 (4-c_a^2)|P'(c_a)|
   \le2\sum_{k=1}^J k|a_k|
   \le2M J(J+1).                                           \tag{24}
\]
This bound includes the small sines at the last double nodes.

The full-high source supplies
\[
 b_{r'a}=(-1)^{r'+a}
   \frac{s_{2a+1}S_{r'}^2}{S_{r'-a}S_{r'+a+1}},\qquad
 |b_{r'a}|\le2,\qquad b_{r'a}=0\ (a>r'),
\]
\[
 \eta(4-c_a^2)R_i'(c_a)
       =\sum_{r'=a}^{m-1}e_{D-r'}(w_i)b_{r'a}.              \tag{25}
\]
By (17), the latter has modulus at most \(2mE_{\alpha_0}\).
Apply (24) to \(L_i\), whose nodal values satisfy (14), and add
(25). The weighted derivative of each \(B_i\) is \(O(N^2)\).
The product rule and (14) give
\((4-c_a^2)|Q'(c_a)|\le C_{\alpha_0}rN^2\).
Apply (24) also to \(P_Q\), and sum over \(a<m\) to obtain (22).
At the finitely many smaller levels, the nodal bounds in this proof
are fixed constants instead of one; compactness absorbs them into
\(C_{\alpha_0,r}\). For \(N=2\), (25) reads \(b_{00}=1\) and follows
directly from \(e_1=-z/4\), so the same proof covers this level.
\(\square\)

## 3. The original alternating high part is retained

There is more structure in (25) than its absolute bound. For every
real \(h_i\ge0\), all the factors \(c_b-w_i\) are negative. Therefore
\[
 \beta_{i,a}:=\eta(4-c_a^2)R_i'(c_a)
       =\eta(-1)^a g_{i,a},\qquad
 g_{i,a}=\sum_{r'=a}^{m-1}
              |e_{D-r'}(w_i)b_{r'a}|>0.                    \tag{26}
\]
This identity holds without a microscopic-height restriction.
The exact angular character is
\[
                    (-1)^a=i^{-D}e^{iN\tau_a/2}.           \tag{27}
\]
Both its constant and its level parity have been retained.

In the full quotient, square-zero nilpotence gives
\[
 Q=\prod_iL_i+\sum_iR_i\prod_{j\ne i}L_j.                   \tag{28}
\]
Consequently (21) is exactly
\[
 \begin{split}
 \gamma_a&=\kappa_a+\eta(-1)^a G_a,\\
 \kappa_a&=\eta(4-c_a^2)
           \left[\left(\prod_iL_i\right)'-P_Q'\right](c_a),\\
 G_a&=\sum_i g_{i,a}\prod_{j\ne i}F_{a,N}(w_j).
 \end{split}                                               \tag{29}
\]
At microscopic heights, \(\sum_a|G_a|\le C_{\alpha_0,r}N^2\);
this follows from (14), (17), and (25). At height zero \(G_a>0\)
when \(r>0\), since all the physical rows at \(2\) are positive.
At nonzero heights the remaining real row factors may have signs.

The correction \(\kappa_a\) is necessary: multiplication of several
low polynomials need not remain in the degree-\(J\) value section.
For one incidence it is zero, but for general valence it has not
been dropped or assigned the character (27). Formula (29), together
with (22), retains both the original alternating high sum and the
additional normal correction introduced by the whole-product fold.

## 4. Charges: symmetric shifts and a fixed-band reset

Use the original canonical cosine coupon \(\mathcal C_{N,\chi}\)
and real-power crossing \(R_n\) from the current source. At each
double node their data are those of
\[
 \cos(N(1-\chi)t),\qquad
 C_{N,n}e^{inNt^2/(4\pi)},\qquad
                 C_{N,n}=e^{\pi i nD^2/(4N)}.              \tag{30}
\]
The odd simple cosine value is one. Thus all scalar carriers remain.
For real \(n\), \(|R_n(c_a)|=1\).

The full-normal cosine product identity gives
\[
 T_k(-z/2)\mathcal C_{N,\chi}
   =\tfrac12(\mathcal C_{N,\chi-k/N}+
                         \mathcal C_{N,\chi+k/N}).         \tag{31}
\]
Inserting (18) in the original trace therefore gives
\[
 \begin{split}
 \phi_N(R_n\mathcal C_{N,\chi}Qf)
 ={}&\sum_{k=0}^J\frac{a_k}{2}
   \left\{L_{n,\chi-k/N}[f]+L_{n,\chi+k/N}[f]\right\}\\
 &+\sum_{a<m}\gamma_a R_n(c_a)\mathcal C_{N,\chi}(c_a)f(c_a),
 \end{split}                                               \tag{32}
\]
where \(L_{n,\chi}[f]=\phi_N(R_n\mathcal C_{N,\chi}f)\).
At unit input charge, the exact symmetry
\(\mathcal C_{N,2-\chi}=\mathcal C_{N,\chi}\) puts both shifts in
\([1-J/N,1]\). The full ordinary convolution of the current source
had bandwidth \(rD\); the value part of (32) has bandwidth \(J\),
independently of \(r\). Its other frequencies have not vanished:
they contribute to the displayed normal term.

For recursion one can do better than shifting a nonunit input.
Let \(P_\chi\) be the degree-\(J\) polynomial interpolating the values
of \(Q\mathcal C_{N,\chi}\) at every distinct node, and write
\[
 P_\chi(z)=\sum_{k=0}^J a_k^\chi T_k(-z/2),\qquad
 d_a^\chi=\eta(4-c_a^2)
       \{(Q\mathcal C_{N,\chi})'-P_\chi'\}(c_a).             \tag{33}
\]
Here a canonical representative may be used for the charged product;
the values and normals defining (33) do not depend on that choice.

**Theorem 2 (charged whole-coupon reduction).** Exactly, for every
complex \(n,\chi\) and every joint spectator \(f\),
\[
 \boxed{\quad
 \phi_N(R_n\mathcal C_{N,\chi}Qf)
   =\sum_{k=0}^J a_k^\chi L_{n,\,1-k/N}[f]
       +\sum_{a<m}d_a^\chi R_n(c_a)f(c_a).
 \quad}                                                    \tag{34}
\]
For real \(\chi\) in any fixed bounded set and heights (10),
\[
             \sum_{k=0}^J|a_k^\chi|\le C_{\alpha_0,r}N,
 \qquad
             \sum_{a<m}|d_a^\chi|
                    \le C_{\alpha_0,r,\chi\text{-bound}}N^3.
                                                               \tag{35}
\]
The output charges \(1-k/N\) always lie in the fixed upper-half
lattice interval \([1-J/N,1]\), irrespective of the real input
charge and of the cut valence. The identity itself is entire in
\(n,\chi\); (35) is a real-parameter estimate.

**Proof.** Subtracting the interpolant gives an element of
\(\mathfrak r_N\), whose trace is the second term by (4).
Moreover \(T_k(-z/2)=\mathcal C_{N,1-k/N}\) as full classes:
their angular values and derivatives coincide, including the odd
simple value. This proves (34), without replacing a normal by a value.

For real \(\chi\), \(|\mathcal C_{N,\chi}(c_a)|\le1\), and its odd
simple value is one. Thus (19) gives the first bound in (35).
The actual charged normal satisfies
\[
 (4-c_a^2)|\mathcal C_{N,\chi}'(c_a)|
    =2N|1-\chi|\,|\sin\tau_a\sin(N(1-\chi)\tau_a)|
    \le2N|1-\chi|.                                        \tag{36}
\]
The product rule, the proof of Lemma 1, and (24) for \(P_\chi\)
give the second bound. Uniform finite-level absorption is as before.
\(\square\)

The alternating high contribution in this version is exactly
\(\eta(-1)^aG_a\mathcal C_{N,\chi}(c_a)\).
The rest of \(d_a^\chi\) is
\(\eta(4-c_a^2)[(\mathcal C_{N,\chi}\prod_iL_i)'-P_\chi'](c_a)\).
Thus (34) does not erase either the charged normals or the phase
identified in (27). It is a representation of the given trace, not
a claim of positivity of its coefficients.

## 5. Actual graph assembly with partial physical evaluations

Use a fixed finite original graph \(G\), selected set \(S\), outside
set \(B\), and arbitrary joint spectator \(A_N\), as in the full-period
current source. No bound on the original degrees is assumed. For a
nonempty removed-current subset \(C\subseteq S\), put
\[
       Y=S\setminus C,\quad G'=G\setminus C,\quad
       W=\{w\in Y:r_w>0\},
                                                               \tag{37}
\]
where \(r_w\) is the number of cut incidences from \(C\) to \(w\).
For fixed integration heights \(\mathbf h\), use the exact coupons
\[
 Q_w(z)=\prod_{\substack{e=vw\\v\in C}}K_N(2\cosh h_v,z),
 \qquad A_{C,\mathbf h}=A_N(\mathbf w_{\mathbf h},
                                      \mathbf z_{V\setminus C}).
                                                               \tag{38}
\]
All parameter dependence of \(A_N\) is held fixed while charge
parameters in the local trace are replaced.

For \(T\subseteq W\) and \(a_w<m\), \(w\in T\), define
\[
 \mathcal Z_{T,\mathbf a}(\boldsymbol\xi)
 =\left(\prod_{v\in Y\setminus T}L_{n_v,\xi_v}^{(z_v)}\right)
  \left[
    A_{C,\mathbf h}\prod_{e\in E(G')}K_N
  \right]_{z_w=c_{a_w}\ (w\in T)} .                         \tag{39}
\]
The graph in (39) is still \(G'\), not \(G'\setminus T\).
In particular every \(T\)--\(T\) edge is
\(K_N(c_{a_v},c_{a_w})\), every edge from \(T\) to a traced vertex
is its physical-row kernel, and every \(T\)--outside edge remains
its evaluated ordinary polynomial. Each evaluated vertex has one
shared physical color across all these factors. Isolated surviving
traces and the original outside data are retained.

Apply (33) to the whole charged coupon at each \(w\in W\), writing
its coefficients \(a_{w,k}^{\chi_w}\) and \(d_{w,a}^{\chi_w}\).
Then the surviving-trace factor of the full current is exactly
\[
 \begin{split}
 &\left(\prod_{v\in Y}L_{n_v,\chi_v}\right)
       \left[A_{C,\mathbf h}\prod_{e\in E(G')}K_N
                                  \prod_{w\in W}Q_w(z_w)\right]\\
 &=\sum_{T\subseteq W}\ 
   \sum_{\substack{0\le a_w<m\ (w\in T)\\
                    0\le k_w\le J\ (w\in W\setminus T)}}
    \left(\prod_{w\in T}d_{w,a_w}^{\chi_w}R_{n_w}(c_{a_w})\right)
    \left(\prod_{w\in W\setminus T}a_{w,k_w}^{\chi_w}\right)
                \mathcal Z_{T,\mathbf a}(\boldsymbol\xi),
 \end{split}                                               \tag{40}
\]
where \(\xi_w=1-k_w/N\) on \(W\setminus T\) and
\(\xi_v=\chi_v\) on \(Y\setminus W\).
This follows by (34) in distinct variables; it does not factor
the joint spectator or any edge connecting two such variables.
Every unconsumed first normal remains inside the traces in (39).
At a vertex in \(T\) the consumed normal is exactly \(d_{w,a_w}\).

For fixed bounded real input charges and arbitrary real surviving
powers, the coefficient norm of the \(T\)-summand is at most
\[
                 C_{G,\alpha_0}N^{\,|W\setminus T|+3|T|}.
                                                               \tag{41}
\]
This is (35) and \(|R_{n_w}(c_a)|=1\).
It bounds the summand by that polynomial times the maximum of the
actual sources (39), over its specified charges and physical colors.
There is no replacement by an absolute unfilled spectator norm.
Identities (39)--(40) hold with unrestricted ordinary outside variables,
and commute with all their fixed derivatives.

Nilpotence restricts the expansion to at most one radical insertion
per surviving vertex. It does not require \(T\) to be an independent
set or the chosen vertices to be endpoints of disjoint original edges.
In particular (40) is not an undirected matching assertion.

## 6. Insertion into the full vertical current

The full-current source proves, with its exact scalar
\(\rho_{N,n,\chi}(h)\) and fixed integration endpoints,
\[
 I_{C,N}=\int_{\prod_{v\in C}[0,H_v]}
   \left(\prod_{v\in C}\rho_{N,n_v,\chi_v}(h_v)\,dh_v\right)
   D_{C,N}(\mathbf h;\mathbf z_B)\,
   \left(\prod_{v\in Y}L_{n_v,\chi_v}\right)
   \left[A_{C,\mathbf h}\prod_{E(G')}K_N\prod_{w\in W}Q_w\right].
                                                               \tag{42}
\]
Here \(D_{C,N}\) retains all internal \(C\)--\(C\) kernels and all
\(C\)--outside kernels. Substitution of (40) in (42) is an exact
finite partially evaluated, half-band charged-source expansion of
the original vertical current. The original inclusion--exclusion
sign \((-1)^{|C|+1}\), crossing carriers and side orientation are
unchanged.

For a quantitative version, let \(e_C\) count internal \(C\)--\(C\)
edges and \(b_{C,B}\) count \(C\)--outside edges. Take
\(H_v=\alpha_v/N\), \(0<\alpha_v\le\alpha_0<\pi\), bounded real
removed powers and input charges, and real outside colors in
\([-2,2]\). Let \(\mathcal M_{T,N}\) be the supremum of the absolute
value of (39) over the integration box, its physical color choices,
and the output charges just specified. Then
\[
 |I_{C,N}|\le
 C_{G,\alpha_0}N^{2e_C+2b_{C,B}}
       \sum_{T\subseteq W}
          N^{|W\setminus T|+3|T|}\mathcal M_{T,N}.           \tag{43}
\]
The constants may also depend on the bounded real parameter boxes.
Indeed the microscopic current corollary gives
\(\int_0^{H_v}|\rho|\,dh\le C\), while each factor of \(D_{C,N}\)
costs \(CN^2\). Equation (41) supplies the remaining factors.
Thus the polynomial exponent from cut incidences at surviving
vertices is replaced by one half-band or normal-channel cost per
such vertex, independently of its cut valence.

Fixed outside derivatives of total order \(|\nu|\) may add
\(2|\nu|\) to the displayed polynomial exponent, with the required
derivatives of (39) included in \(\mathcal M_{T,N}\). This follows
from the microscopic real-color Markov bounds on the cut kernels
and the ordinary product rule. No derivative of a free outside
spectator has been silently bounded.

Equations (40)--(43) are compatible with repeated full-trace current
expansion: input lattice charges stay legitimate, and each newly
folded traced vertex returns to the same upper-half lattice.
Untouched vertices keep their original charges. Thus unit or already
upper-half lattice inputs give a recursively closed traced charge set.
For arbitrary starting real charges, one may also apply (34) with
\(Q=1\) at any initially untouched vertex, retaining its corresponding
normal branch and polynomial cost; that additional operation is not
implicit in (40).
The additional physical-evaluation branches and their shared kernels
must still be carried. Their coherent action estimates, and the
comparison with the compatible classical saturated face, are not
provided by this polynomial reduction.

## 7. Coverage and direct-source readback

The exact low/high radical contraction and its shared physical
evaluations precede this note. The new point is to interpolate the
whole product at a shared survivor, and then the whole charged product,
so the traced frequency band is independent of the original cut
valence while every additional normal is explicit. The original
alternating high character is separated from the new low-product
normal correction. The current being reduced is the full-\(\pi\)
vertical current, not the one-step Ward current or a replacement
of the original scalar by a positive norm.

The following three complete direct sources were read and their used
implications and hashes checked:

* [Full-period current and charge convolution](research_full_period_current_charge_convolution.md),
  SHA256 3f74b9824ecbf0b71a79b17959c7208f650103f95932192cfba87c7a7aa05595:
  original carriers and full-normal charge data; symmetric charge
  product identity; full-survivor graph/current formula; microscopic
  current and edge bounds.
* [Coherent endpoint kernel reduction](research_full_period_endpoint_kernel_reduction.md),
  SHA256 a1d67ac803c0160bbfdacaa96a6fde9dc1ffae06fc39eb94f0416dcf2ecef76e:
  physical-row root disk, both-parity cosine interpolation, ordinary
  mixed derivatives, odd simple trace and \(N=2\) normalization.
* [Full high Newton radical](research_high_newton_radical_contraction.md),
  SHA256 1faa5d2e02edf0a1462cc43b243e0ab4403bf56e9f1af0befb6b492441d9dd03:
  square-zero full physical radical, exact divided-difference
  coefficients and their signs/bounds, and the shared physical-value
  contraction retaining all unchosen edges.

Only written proofs, text reads and hashes were used. No mathematical
program, numerical experiment, test or compilation was run. Frozen
notes and public manuscripts are unchanged.
