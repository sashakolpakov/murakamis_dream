# A complete conditional ceiling near the incoming unit endpoint

Private written deduction, 10 November 2026. A thin rectangle before the
incoming numerator wall controls the original critical integral and every
associated finite cotangent correction. All other physical rows, including
every postwall row, remain in an explicit positive block. This gives a
complete conditional upper bound on compact intervals sufficiently close
to the incoming endpoint.

The additional middle physical block in this theorem is not paid here.
In particular, this is neither dominance of the critical action nor a
completion of the remaining right outer interval.

## 1. Original source and the complete ceiling

Keep the original type-four conditional source from
[the torus identity, equation (1)](research_mixed_conditional_torus_composition.md):
\[
 q_N=e^{-2\pi i/N},\qquad P_j=(q_N;q_N)_j,\qquad
 p_j(Z)=(q_NZ;q_N)_j,\qquad
 C_{1,N}(X,Y)=\sum_{j=0}^{N-1}
                   \frac{X^{-j}p_j(X)p_j(Y)}{P_j^3}.
 \tag{1}
\]
There is no change of polynomial, incoming carrier, index set or parity.
For this note use the closed actual outgoing container
\[
 \mathcal B=\left\{b=z+id:
       \frac{11}{50}\le z\le\frac9{20},\quad
       -\frac{51}{500}\le d\le-\frac1{1000}\right\},
 \qquad Y=e^{-2\pi ib}.
 \tag{2}
\]
Thus the outgoing \(Y\)'s form a compact subset of
\(\{\Im Y<0,\ \Re Y<1,\ |Y|<1\}\).
Put
\[
 a=1-\delta,\qquad X=e^{2\pi i\delta},\qquad
 Q(s;a,b)=g(a+s)+g(b+s)-3g(s)-g(a)-g(b)+2\pi ias.
 \tag{3}
\]
The primitive and all logarithms are original:
\[
 g'(w)=\operatorname{Log}(1-e^{-2\pi iw}),\qquad 0<\Re w<1.
\]
Let \(s_*=u_*+ih_*\) be the original critical point from the
[unit incoming branch theorem](research_mixed_four_conditional_unit_incoming_branch.md),
and let \(\Theta(a,b)=Q(s_*;a,b)\).

Define continuous, zero-safe real rates by
\[
 \begin{split}
 J(t)&=\int_0^t\log(2\sin\pi v)\,dv,\\
 I_a(t)&=\int_0^t\log|1-e^{-2\pi i(a+v)}|\,dv,\\
 I_b(t)&=\int_0^t\log|1-e^{-2\pi i(b+v)}|\,dv,\\
 E(t;a,b)&=I_a(t)+I_b(t)-3J(t),\qquad 0\le t\le1.
 \end{split}
 \tag{4}
\]
Integrable logarithmic zeros use their continuous integral values.
The endpoint \(t=1\) is a continuous rate, not an added finite row.
Since \(a\) is real, the incoming carrier in (1) has modulus one.

**Theorem 1.** There is a fixed \(\delta_0>0\) such that, for every
\(0<\varepsilon\le\delta_0\), every \(\tau>0\), and all sufficiently
large \(N\),
\[
 \begin{split}
 |C_{1,N}(e^{2\pi i\delta},e^{-2\pi ib})|
 &\le C_{\varepsilon,\tau}N^{A_{\varepsilon,\tau}}
          e^{N\{\mathcal M(\delta,b)+\tau\}},\\
 \mathcal M(\delta,b)
 &=\max\left\{\Re\Theta(1-\delta,b),\quad
       \max_{t\in[0,\delta/2]\cup[\delta-\delta^4,1]}
                             E(t;1-\delta,b)\right\},
 \end{split}
 \tag{5}
\]
uniformly for \(\varepsilon\le\delta\le\delta_0\), \(b\in\mathcal B\),
at both level parities.

The proof retains every physical row outside the displayed prewall
interval, the original unweighted critical horizontal and its two joins,
and all six weighted cotangent currents. Neither the constants in (5)
nor the onset in \(N\) are asserted to be uniform as
\(\varepsilon\downarrow0\).

The previously controlled physical groups \(t\le2/25\) and \(t\ge1/2\)
do not exhaust the second alternative in (5). For small \(\delta\),
the entire interval \([\delta-\delta^4,1/2]\), in particular its
postwall middle part, is still present. No comparison of this part with
the original attached geometric rate is inferred.

## 2. A fixed prewall interval containing the actual critical point

The original endpoint factorization in
[the endpoint root theorem, equations (2) and (11)](research_mixed_four_conditional_unit_endpoint_factorization.md)
is
\[
 v=X+(1-X)^3f(X,Y),\qquad f(1,Y)=\frac1{Y-1},
 \qquad s_*=\frac{\operatorname{Log}v}{2\pi i}.
 \tag{6}
\]
Here \(f\) is holomorphic on a fixed neighborhood of the endpoint
and the outgoing compact set. The logarithm is the original upper-root
lift. Expanding the holomorphic factors, with uniform remainders, gives
\[
 (1-X)^3=8\pi^3i\delta^3+O(\delta^4),\qquad
 s_*=\delta+\frac{4\pi^2}{Y-1}\delta^3+O(\delta^4).
 \tag{7}
\]
Indeed, divide (6) by \(X\) and use
\(\operatorname{Log}v=\operatorname{Log}X+
 \log(1+(1-X)^3f/X)\), where \(\operatorname{Log}X=2\pi i\delta\).
This also verifies the sign and the coefficient in (7).

On the outgoing compact set,
\(\Re(1/(Y-1))=(\Re Y-1)/|Y-1|^2<0\).
Its negative has a positive minimum. Consequently, after decreasing
\(\delta_0\), there are fixed \(c_0,M_0>0\) such that
\[
 \frac{\delta}{2}<u_*<\delta-c_0\delta^3
       <\delta-\delta^4,\qquad
 |h_*|\le M_0\delta^3<\frac{\delta^2}{4}.
 \tag{8}
\]
All inequalities are strict and uniform in (2). Set
\[
             \ell=\frac{\delta}{2},\qquad
             r=\delta-\delta^4,\qquad H=\delta^2.
 \tag{9}
\]
Thus the cuts are independent of the outgoing parameter. Every argument
in (3) has real part in \((0,1)\) throughout
\(\ell\le\Re s\le r,\ |\Im s|\le H\).
In particular, the core never crosses either numerator wall.

We shall decrease \(\delta_0\) a finite number of further times below.
All choices are made before \(\varepsilon\), \(\tau\), or \(N\).

## 3. Curvature and argument bounds on the whole thin rectangle

For \(w=u+i\sigma\) in the original strip write
\[
 \mathcal C(w)=\Re\cot(\pi w)
     =\frac{\sin(2\pi u)}
            {\cosh(2\pi\sigma)-\cos(2\pi u)},\qquad
 \mathcal A(w)=\Arg(1-e^{-2\pi iw}).
 \tag{10}
\]
The following estimates also hold on the slightly larger real interval
\[
             \frac{\delta}{3}\le u\le\delta-\frac{\delta^4}{2},
                   \qquad |\sigma|\le\delta^2,
 \tag{11}
\]
which will accommodate the finite half-grid cuts.

First,
\[
             \mathcal C(u+i\sigma)\ge\frac1{2\pi u}
                                  \ge\frac1{2\pi\delta}.
 \tag{12}
\]
Here is a direct uniform justification. Taylor expansions at zero give
\[
 \frac{\sin(2\pi u)}{2\pi u}=1+O(\delta^2),\qquad
 \frac{\cosh(2\pi\sigma)-\cos(2\pi u)}{2\pi^2u^2}
       =1+\frac{\sigma^2}{u^2}+O(\delta^2)
       =1+O(\delta^2),
 \tag{13}
\]
because \(|\sigma|/u\le3\delta\). Their remainders are uniformly
bounded by the elementary derivatives of sine, cosine and hyperbolic
cosine on a fixed neighborhood of zero. Thus
\(\pi u\mathcal C=1+O(\delta^2)\), which proves (12) after shrinking
\(\delta_0\). This is an analytic limit argument, not an evaluation.

The incoming real part \(a+u\) lies in \((1/2,1)\), so
\(\mathcal C(a+s)<0\), at either sign of \(\sigma\).
The outgoing real part lies in a fixed compact subset of \((0,1/2)\)
if \(\delta_0<1/20\); the outgoing heights remain bounded. Hence
\(|\mathcal C(b+s)|\le M_1\) for a fixed constant \(M_1\).
Since \(g''(w)=\pi\cot(\pi w)-\pi i\), (12) gives
\[
 -\Re Q_{ss}
   =\pi\{3\mathcal C(s)-\mathcal C(a+s)-\mathcal C(b+s)\}
   \ge\frac{3}{2\delta}-\pi M_1
   \ge\frac1{\delta}>0 .
 \tag{14}
\]
Thus \(R(u,\sigma)=\Re Q(u+i\sigma)\) is strictly concave in \(u\)
and strictly convex in \(\sigma\) on (11).

Second, uniformly on (11),
\[
                     \frac{5\pi}{12}<\mathcal A(s)<\frac{7\pi}{12}.
 \tag{15}
\]
Indeed,
\[
 \frac{1-e^{-2\pi i(u+i\sigma)}}{2\pi iu}
      =1+i\frac{\sigma}{u}+O(\delta)=1+O(\delta).
 \tag{16}
\]
The quotient stays close to the positive real number one, while
\(2\pi iu\) has argument \(\pi/2\). The original continuous strip
argument therefore satisfies (15).

At the incoming numerator,
\(-\pi<\mathcal A(a+s)<0\), because \(1/2<a+u<1\).
Choose \(\delta_0\) also so small that
\[
               \sup_{b\in\mathcal B}|Y|\,e^{2\pi\delta_0^2}<1.
 \tag{17}
\]
Since \(0<\Re(b+s)<1/2\), this gives
\(0<\mathcal A(b+s)<\pi/2\).
Differentiating the original phase without changing a lift now yields
\[
 \begin{split}
 I(u,\sigma):=\Im Q_s
    &=\mathcal A(a+s)+\mathcal A(b+s)-3\mathcal A(s)+2\pi a,\\
 -\pi&<-\frac{3\pi}{4}-2\pi\delta<I(u,\sigma)
                        <\frac{5\pi}{4}<\frac{3\pi}{2},
 \end{split}
 \tag{18}
\]
where \(\delta_0<1/8\) is sufficient for the lower comparison.
In particular \(|I|<3\pi/2\). This estimate keeps the full
incoming chirp \(2\pi ias\).

## 4. The exact finite interpolation and integer partition

Use the original numerator and reciprocal from
[the joint global chart, equations (2), (4), and (6)](research_mixed_fourier_right_cap_joint_global_chart.md):
\[
 \Pi_N(w)=G_N(Nw)
   \exp\!\left\{\frac{\pi i}{2}[N(w-w^2)-w]\right\},\qquad
 E_N(w)=\frac1{\Pi_N(w)}\quad(0<\Re w<1).
 \tag{19}
\]
The canonical \(G_N\) and its original compact-strip expansion are those
of [the exact factorial construction, Sections 1 and 4](exact_factorial_interpolation_and_complex_contours.md).
The exact conditional interpolant is
\[
 T_N(s;a,b)=e^{2\pi iNas}\Pi_N(a+s)\Pi_N(b+s)
                            E_N(a)E_N(b)E_N(s)^3.
 \tag{20}
\]
The recurrence in the joint chart shows, for every retained integer,
\[
 T_N(j/N;a,b)=\frac{X^{-j}p_j(X)p_j(Y)}{P_j^3}.
 \tag{21}
\]
For each fixed \(\varepsilon>0\), all arguments on the rectangles in
Section 3 stay in fixed regular compact strips. The canonical
factorial expansion therefore implies
\[
              |T_N(s;a,b)|\le C_\varepsilon N^{A_\varepsilon}
                                      e^{N R(s;a,b)}
 \tag{22}
\]
on those rectangles, uniformly for the specified parameters.
No period recurrence or discarded numerator multiplier is needed there.

Let
\[
 \begin{aligned}
 L_N&=\lfloor N\ell\rfloor+1,&
 M_N&=\lceil Nr\rceil,\\
 \ell_N&=(L_N-\tfrac12)/N,&
 r_N&=(M_N-\tfrac12)/N .
 \end{aligned}
 \tag{23}
\]
For sufficiently large \(N\), depending on \(\varepsilon\),
\(\ell_N<u_*<r_N\), both cuts lie in (11), and the entire rectangle
between them remains prewall. All original rows split exactly as
\[
 C_{1,N}=
 \sum_{0\le j<L_N}\frac{X^{-j}p_j(X)p_j(Y)}{P_j^3}
 +\sum_{L_N\le j<M_N}T_N(j/N)
 +\sum_{M_N\le j<N}\frac{X^{-j}p_j(X)p_j(Y)}{P_j^3}.
 \tag{24}
\]
In particular the upper block starts before the incoming wall.

The zero-safe product argument in
[the complete physical upper-block proof, Section 2](research_mixed_conditional_lower_output_upper_block.md)
applies to every index here. More explicitly, truncating a numerator
logarithm below \(-\log N\) gives total variation \(O(\log N)\)
and an integral change \(O(1/N)\), uniformly in its real shift.
For the outgoing factor the radius stays strictly below one.
The denominator has
\(\log|P_j|=NJ(j/N)+O(\log N)\), uniformly up to \(j=0,N-1\).
Thus each of the physical summands in (24) has the upper bound
\[
 \left|\frac{X^{-j}p_j(X)p_j(Y)}{P_j^3}\right|
       \le C N^A e^{N E(j/N;a,b)} .
 \tag{25}
\]
This remains valid when a numerator is zero. Continuity of the
integrated rates, including their wall and endpoint values, implies that
both outer sums in (24) are bounded by the second alternative in (5),
with any prescribed positive rate tolerance for the cut displacements.

## 5. Every core current

Take the rectangle in (23) at heights \(\pm H\), with \(H=\delta^2\).
The exact split-cotangent formula is the one in
[the original middle reduction, equation (15)](research_mixed_conditional_lower_output_middle_reduction.md):
\[
 \begin{split}
 \sum_{j=L_N}^{M_N-1}T_N(j/N)
    &=N\int_{\ell_N}^{r_N}T_N(t)\,dt+\mathcal R_N,\\
 \mathcal R_N&=\frac{N}{2i}\left\{
   \int_{\partial R^+_{\rm off}}T_N(s)[\cot(\pi Ns)+i]\,ds+
   \int_{\partial R^-_{\rm off}}T_N(s)[\cot(\pi Ns)-i]\,ds
                               \right\}.
 \end{split}
 \tag{26}
\]
Each off-real boundary has its induced positive-boundary orientation:
the upper one runs up the right side, left along the top, and down
the left side; the lower one runs down the left side, right along
the bottom, and up the right side. These are precisely two horizontal
and four vertical half-currents. The coefficient \(N/(2i)\), and
the zero-mode coefficient \(+N\), are unchanged.

The original holomorphic interpolant also gives the exact identity
\[
 \int_{\ell_N}^{r_N}T_N(s)\,ds
   =\int_{\ell_N}^{\ell_N+ih_*}T_N(s)\,ds
    +\int_{\ell_N+ih_*}^{r_N+ih_*}T_N(s)\,ds
    +\int_{r_N+ih_*}^{r_N}T_N(s)\,ds .
 \tag{27}
\]
The original zero lift gives \(Q_s(s_*)=0\).
Strict horizontal concavity in (14) therefore shows
\[
              R(u,h_*)\le R(u_*,h_*)=\Re\Theta(a,b)
                  \qquad(\ell_N\le u\le r_N).
 \tag{28}
\]
At either real cut, vertical convexity bounds the unweighted join by
the larger of its real endpoint and its critical-height endpoint.
By (28), the latter is at most \(\Re\Theta\); the former tends uniformly
to \(E(\ell;a,b)\) or \(E(r;a,b)\).
The three currents in (27), with their original \(+N\) measure, thus
have rate at most \(\mathcal M+\tau\).

For the four weighted vertical halves, the exact half-grid kernel
bound is
\[
 |\cot(\pi Ns)+i|\le2e^{-2\pi N\sigma}\quad(\sigma\ge0),\qquad
 |\cot(\pi Ns)-i|\le2e^{2\pi N\sigma}\quad(\sigma\le0).
 \tag{29}
\]
Since \(R_\sigma=-I\), (18) shows that \(R-2\pi\sigma\)
strictly decreases on each upper half, while \(R+2\pi\sigma\)
strictly increases on each lower half. Each is therefore bounded by
its real-cut rate. This pays the whole weighted half-side by the
corresponding physical-rate alternative of (5), including its
endpoint at zero height.

On the top and bottom, the same kernels have bounds
\(4e^{-2\pi NH}\) once \(N\) is sufficiently large. From (18),
(28), and \(|h_*|<H/4\),
\[
 \begin{split}
 R(u,\pm H)-2\pi H
 &\le R(u,h_*)+\frac{3\pi}{2}(H+|h_*|)-2\pi H\\
 &\le\Re\Theta-\frac{\pi H}{8}.
 \end{split}
 \tag{30}
\]
Thus both complete horizontal aliases have a strict rate loss,
at least \(\pi\varepsilon^2/8\) before any optional tolerance.
No height is sent to infinity, and no alias denominator is dropped.

Equations (22)--(30), followed by the exact partition (24), prove
Theorem 1. All constants are uniform on the stated compact parameter
family. The finitely many earlier levels can be included by enlarging
the polynomial prefactor if desired.

## 6. Scope of the improvement

The theorem is a finite-source consequence of the endpoint branch,
with every postwall and endpoint row retained. It does not try to
continue the older postwall force bound to a region where it fails.
The critical source is controlled because its own cotangent grows
like \(1/\delta\) on a rectangle of height \(\delta^2\), whereas
the actual critical height is only \(O(\delta^3)\).

The physical maximum in (5) is an explicit outstanding comparison.
Neither its additional middle interval nor its product with the
complete cap is shown to lie below the original affine rate here.
The theorem also does not bridge the remaining interval from \(a=.7\)
to its sufficiently small endpoint neighborhood. An exact source
identity may multiply (24)--(27) by the original cap, diagonal weight,
selected monomial and outgoing halfweight; those factors have not
been divided out or estimated by this conditional statement.
There is no new nonzero coefficient, full outer-period or knot claim.

## Frozen source bindings

| Direct source | SHA-256 |
|---|---|
| research_mixed_conditional_torus_composition.md | 8a25a25a95bf11767c4f305317a6fab9a9c17724ae0e24a36014b5fd8ec4f693 |
| research_mixed_four_conditional_unit_incoming_branch.md | b6c8fdaffd436ec82670ec864629d93d36e7c7a8ae7e81033b684e3f86e92e43 |
| research_mixed_four_conditional_unit_endpoint_factorization.md | 7eeb4d3188955e37029875d8612cb235dbf9fc0118828b5818c52ed0e8fad33d |
| research_mixed_fourier_right_cap_joint_global_chart.md | bf0069e52715e82c34be008c5814373017b43c019dd2a1a71dcd381e96b4da9f |
| exact_factorial_interpolation_and_complex_contours.md | 1f34f65437dfe0bfb4062a7a74840beae1676353cf13bb8a86f8849a8a36bc72 |
| research_mixed_conditional_lower_output_middle_reduction.md | 9df0e7cdf4a193783e236e8e0fa8f416b5a123d8afe02033601be333cf6d5bc7 |
| research_mixed_conditional_lower_output_upper_block.md | 9cb348fc186cb9bf3768b5915baf2aa1d952588ca3b89d8cfab422f7cf1303cd |
