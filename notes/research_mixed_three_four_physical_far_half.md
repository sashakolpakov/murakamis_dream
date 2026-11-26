# Physical far-half bounds for the original three/four pair

Research deduction, 7 November 2026. No numerical evaluation is used.
The first result bounds the whole type-three cap at every sampled
incoming root on the far half-circle. The second pays the complete
sampled-root sector with incoming index at least \(5N/6\), using the
coherent private endpoint source inside the type-four factor. These
are physical-index estimates. A partial root sum is not identified
with an integral over a corresponding arc.

## 1. Literal sources and uniform physical-product bounds

Use the conventions of the
[actual ordinary three/four target](research_mixed_three_four_ordinary_pair_target.md),
Section 2:
\[
 D=N-1,\quad r=e^{-2\pi i/N},\quad q=e^{\pi i/N},\quad
 P_j=(r;r)_j,\quad S_j=|P_j|,\quad p_j(X)=(rX;r)_j .
 \tag{1}
\]
The full ordinary polynomials are
\[
\begin{split}
 H_N(w,Y)&=\sum_{\ell=0}^{D}
       \frac{(-q)^{-\ell}e_\ell(w)}{P_\ell}(Y;r)_\ell,\\
 U_{\alpha,N}(w,X)&=\sum_{j=0}^{D}
       \frac{H_N(w,r^{-j})p_j(X)}{P_j^{1+\alpha}},\\
 V_{1,N}(w,X)&=\sum_{i=0}^{D}
       \frac{X^{-i}p_i(X)}{P_i^2}U_{1,N}(w,r^i).
\end{split}
 \tag{2}
\]
The exact original observation is
\[
 Z_{34,N}(w_L,w_R)
 =\kappa_N^3N\sum_{b=0}^{D}
       U_{0,N}(w_L,r^b)V_{1,N}(w_R,r^b).
 \tag{3}
\]
Here \(\kappa_N\) is the original unit-modulus scalar. In particular,
there is no additional retained \(d_N\) weight or Fourier selection
in (3).

Write
\[
 J(t)=\int_0^t\log(2\sin\pi u)\,du,\qquad 0\le t\le1.
 \tag{4}
\]
The original uniform sine-product estimates give
\(\log S_j=NJ(j/N)+O(\log N)\), uniformly for \(0\le j<N\).
They include \(j=0,D\). We use
\[
 J(1-t)=-J(t),\qquad J(1/2)=0,\qquad
 J'(t)=\log(2\sin\pi t).
 \tag{5}
\]
The [zero-safe Newton tube theorem](research_mixed_newton_color_tubes.md),
Sections 1--2, gives, for every prescribed \(\tau>0\), a fixed
ordinary disk about \(-2\) on which
\[
 |e_\ell(w)|\le C N^A
   \exp N\{V_0(\ell/N)+\tau\},\qquad
 V_0(u)=-2J(1/2-u)-2J(u),\quad 0\le\ell/N\le1/2.
 \tag{6}
\]
This is an upper bound even at a vanished Newton factor. Uniform
holomorphy gives every fixed ordinary derivative on a smaller disk.
All tolerance symbols below can be divided among finitely many
uses before choosing this disk.

## 2. A whole physical type-three ceiling

The exact terminating identity in
[the physical type-three cap theorem](research_mixed_three_first_cap_packet.md),
Lemma 1, is
\[
 U_{0,N}(w,r^b)
  =\frac{N}{P_b^2}
     \sum_{\ell=0}^{D-b}(-q)^{-\ell}e_\ell(w)
                         \frac{P_{b+\ell}}{P_\ell^2}.
 \tag{7}
\]
It holds for the whole ordinary polynomial and both level parities.
No factorial in this support vanishes. The rows beyond it vanish
in the original physical source; no off-grid termination is asserted.

Put \(v=1-b/N\) and \(u=\ell/N\). For \(b/N\ge1/2\),
\(0\le u\le v-1/N< v\le1/2\). Equations (5)--(7) give the
uniform row upper rate
\[
 Q(v,u)=-2J(1/2-u)-4J(u)-J(v-u)+2J(v),
       \qquad 0\le u\le v\le1/2.
 \tag{8}
\]
The added boundary \(u=v\) is used only for an upper envelope.
In the open interval \(0<u<v\),
\[
\begin{split}
 Q_u&=\log\frac{\cos^2(\pi u)\sin\pi(v-u)}
                         {2\sin^4(\pi u)},\\
 Q_{uu}&=-2\pi\tan\pi u-4\pi\cot\pi u-\pi\cot\pi(v-u)<0.
\end{split}
 \tag{9}
\]
The endpoint derivatives are \(+\infty\) and \(-\infty\), so
there is a unique interior maximum \(u_*(v)\). It is below \(1/4\).
For \(v\le1/4\) this is immediate; for \(v>1/4\), substituting
\(u=1/4\) in (9) gives a ratio at most \(1/\sqrt2<1\).

At the maximum,
\[
 \sin\pi(v-u_*)=\frac{2\sin^4\pi u_*}{\cos^2\pi u_*}.
\]
Consequently the differentiable maximum obeys
\[
 \frac{d}{dv}Q(v,u_*(v))
 =\log\frac{\sin^2\pi v\,\cos^2\pi u_*}{\sin^4\pi u_*}
 >\log\cot^2\pi u_*>0.
 \tag{10}
\]
We used \(u_*<v\le1/2\). Thus the entire envelope is bounded
by its value at \(v=1/2\).

Let \(c_*=-J(1/4)\). At \(v=1/2\),
\[
\begin{split}
 Q(1/2,u)&=-3J(1/2-u)-4J(u),\\
 Q(1/2,1/4)&=7c_*,\qquad Q_u(1/2,1/4)=-\tfrac12\log2,\\
 Q_{uu}(1/2,u)&=-\pi(3\tan\pi u+4\cot\pi u)
                                      \le-4\pi\sqrt3 .
\end{split}
 \tag{11}
\]
The resulting quadratic upper support gives
\[
 \max_{u}Q(1/2,u)
 \le 7c_*+\frac{(\log2)^2}{32\pi\sqrt3}<\frac{41}{40}.
 \tag{12}
\]
For the final strict inequality, the existing scalar
\(-4J(1/4)<73/125\), recorded in
[the endpoint seam majorants](research_mixed_endpoint_seam_majorants.md),
Section 2, gives \(7c_*<511/500\). Also
\(\log2<7/10\), \(\pi>157/50\), and \(\sqrt3>5/3\) give
\[
 \frac{(\log2)^2}{32\pi\sqrt3}
       <\frac{735}{251200}<\frac3{1000}.
 \tag{13}
\]
The logarithm bound follows, for example, from
\(1+7/10+49/200+343/6000>2\).

**Theorem 1.** For every \(\tau>0\) and fixed ordinary derivative
order \(k\), a sufficiently small fixed disk about \(-2\) has
\[
 |\partial_w^k U_{0,N}(w,r^b)|
 \le C_k N^{A_k}\exp N\left(\frac{41}{40}+\tau\right),
       \qquad \lceil N/2\rceil\le b<N.
 \tag{14}
\]
This is the whole original cap at each indicated physical root.
It holds at both parities. It is not a pointwise bound on an
off-grid far arc or on a complex incoming-height contour.

## 3. Retain the complete private source in the type-four factor

The [coherent seam source theorem](research_mixed_cap_seam_source_bounds.md),
Theorem 1 with \(\epsilon=1\), gives
\[
 \sum_{j=0}^{D}\frac{|H_N(w,r^{-j})|}{S_j}
 \le C N^A\exp N\left(\frac{433}{500}+\tau\right).
 \tag{15}
\]
Indeed its exact normalization is
\(H_N(w,r^{-j})=P_jD_N(j/N)^{-1}\mathcal C_N(j/N,w)\),
where the physical \(D_N\) has modulus one. Thus (15) keeps
the entire Newton sum in every \(H_N\).

At a physical transform row \(i\), the source (2) is exactly
\[
 U_{1,N}(w,r^i)
 =\sum_{j=0}^{D-i}
   \frac{H_N(w,r^{-j})}{P_j}
   \frac{P_{i+j}}{P_iP_j}.
 \tag{16}
\]
Put \(t=i/N\) and \(e=j/N\). The last quotient has rate
\(J(t+e)-J(t)-J(e)\). On \(0\le e\le1-t\), its maximum is
\[
 L(t)-J(t),\qquad L(t)=-2J((1-t)/2).
 \tag{17}
\]
For \(0<t<1\), differentiate with respect to \(e\): the sign is
that of \(\sin\pi(t+e)-\sin\pi e\), positive before
\((1-t)/2\) and negative after. The endpoint \(t=0\) has
constant value zero. Uniform physical factorial bounds therefore
give, without division by \(H_N\),
\[
 |U_{1,N}(w,r^i)|
 \le C N^A\exp N\left\{\frac{433}{500}
                               +L(t)-J(t)+\tau\right\}.
 \tag{18}
\]
For \(0\le t\le1/2\), the integral expression in (17) gives
\[
 L(t)=2\int_{(1-t)/2}^{1/2}\log(2\sin\pi u)\,du
                                                 \le t\log2.
 \tag{19}
\]

## 4. Payment of the complete physical sector \(b/N\ge5/6\)

Set \(v=1-b/N\le1/6\). In (7), \(0\le u\le v\).
Since \(J\) decreases on \([0,1/6]\), (8) and (19) imply
\[
 Q(v,u)\le2v\log2-3J(v).
 \tag{20}
\]
Explicitly, the first term of (8) is at most \(2u\log2\);
\(-4J(u)\le-4J(v)\); and
\(-J(v-u)+2J(v)\le J(v)\).

In the full terminal source, \(p_i(r^b)=0\) for \(i+b\ge N\).
For \(0\le i\le D-b\), its remaining exact factor is
\[
 \frac{r^{-bi}P_{b+i}}{P_bP_i^2}.
 \tag{21}
\]
The chirp \(r^{-bi}\) has modulus one, and its rate in absolute
value is
\[
 J(v)-J(v-t)-2J(t),\qquad t=i/N\le v-1/N.
 \tag{22}
\]
Combining (18), (19), and (22) gives, for every retained transform
row, the upper rate
\[
\begin{split}
 \frac{433}{500}+L(t)+J(v)-J(v-t)-3J(t)
 \le \frac{433}{500}+v\log2-3J(v).
\end{split}
 \tag{23}
\]
Here \(J(v)-J(v-t)\le0\) and \(-J(t)\le-J(v)\).
All physical transform rows and all coherent private sources are
included. Their number contributes only a polynomial factor.

The full product therefore has upper rate
\[
 \frac{433}{500}+3v\log2-6J(v).
 \tag{24}
\]
This increases on \(0\le v\le1/6\). Concavity of sine on that
interval gives \(2\sin\pi t\ge6t\), hence
\[
 J(1/6)\ge\int_0^{1/6}\log(6t)\,dt=-1/6.
 \tag{25}
\]
Equations (24)--(25) and \(\log2<7/10\) prove the strict
uniform ceiling
\[
 \frac{433}{500}+\tfrac12\log2+1
                                  <\frac{277}{125}.
 \tag{26}
\]

Let \(M\) denote the actual ordinary \((3,4)\) critical action
at complete colors, with the unchanged primitive and allocation.
The [two-vertex first-collar proof](research_mixed_two_vertex_first_collar.md),
equation (15), establishes
\[
 M>\frac94-\frac{147\pi}{20000}
    >\frac{22269}{10000},\qquad
 \frac{22269}{10000}-\frac{277}{125}
                                  =\frac{109}{10000}>\frac1{100}.
 \tag{27}
\]
The second inequality uses \(\pi<22/7\). It is a comparison to
the actual paired source action, not a sum of unrelated cap floors.

**Theorem 2.** On a sufficiently small fixed ordinary-color
bidisk about \((-2,-2)\), every fixed pair of ordinary derivative
orders satisfies
\[
 \left|\partial_{w_L}^{k}\partial_{w_R}^{\ell}
  \left[\kappa_N^3N
    \sum_{b=\lceil5N/6\rceil}^{N-1}
        U_{0,N}(w_L,r^b)V_{1,N}(w_R,r^b)\right]\right|
 \le C_{k,\ell}N^{A_{k,\ell}}
                  e^{N(M-1/200)}.
 \tag{28}
\]
The same estimate bounds the sum of the absolute values of the
individually differentiated products, with the external factor
\(|\kappa_N^3N|=N\). To prove it, first reserve less than
\(1/200\) of the strict margin in (27) for the combined
ordinary-color tolerances in (6) and (15), and then use Cauchy's
formula on a smaller bidisk. Every exact finite support and the
chirp in (21) are preserved, including the final row \(b=D\).
Empty small-level sectors cause no exception. Both level parities
have the same proof.

## 5. Scope of the physical deletion

Equation (28) permits deletion of precisely this complete sampled
sector from the exact root sum (3), with the stated controlled
error. It does not bound a continuous incoming arc, supply a
complex incoming-height packet, or replace either coherent factor
by an absolute-row envelope at another incoming point.

The remaining sampled rows \(b/N<5/6\) still form their own exact
finite sum. If that partial sum is represented by a cardinal
contour, all of its sampling aliases, true endpoints, and joining
currents must be retained. Neither the full-circle constant-term
identity nor the physical termination in (7), (16), and (21)
removes those currents. No whole \((3,4)\) packet or new knot-family
conclusion follows from the present physical-sector estimate alone.
