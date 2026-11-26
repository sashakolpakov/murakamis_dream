# Real-row bounds for the original outer endpoint cap

Research lemma, 5 November 2026. These estimates concern the literal
outer rows, including the Pochhammer rows that revive at a complex
outgoing index. No terminating type-three replacement is made.
They reduce both real tails to their cut values and fixed endpoint
ceilings. Comparing those quantities with the selected cap action, and
bounding the outer contour currents, remain separate requirements.

## 1. The finite rows and their rates

Put \(r=e^{-2\pi i/N}\), \(P_i=(r;r)_i\),
\(p_i(X)=(rX;r)_i\), and \(X=e^{-2\pi iz}\). For
\(\epsilon=0,1\), the exact cap polynomial from
[torus composition](research_mixed_conditional_torus_composition.md),
equations (17), (21), is
\[
 \mathcal U_{\epsilon,N}(w,X)=\sum_{i=0}^{N-1}B_{i,N}^{\epsilon}(w,z),
 \qquad
 B_{i,N}^{\epsilon}
 =\Delta_N(i/N)^{-1}C_N(i/N,w)\frac{p_i(X)}{P_i^\epsilon},
                                                               \tag{1}
\]
where
\[
 \Delta_N(s)=\exp\{\pi i[N(s-s^2)-s]/2\}.
                                                               \tag{2}
\]
The coefficient \(C_N\) is the original canonical endpoint sum.
Indeed \(G_N(i)=S_i\), \(P_i=\Delta_N(i/N)S_i\), and the exact
identity \(\mathcal H_N(w,r^{-i})=S_iC_N(i/N,w)\) proves (1).
In particular \(|\Delta_N(s)|=1\) on real rows.

Use the [certified attached rectangles](research_mixed_open_word_endpoint_rectangles.md)
\[
\begin{split}
 T_3&=[.278,.391]+i[-.072,.021],\\
 T_4&=[.246,.350]+i[-.108,-.020].
\end{split}                                                   \tag{3}
\]
Their closed versions are convenient containing sets. Write \(z=x+ih\),
\(h_+=\max(h,0)\), and define
\[
\begin{split}
 L_h(t)&=\log|1-e^{-2\pi i(t+ih)}|
 =\pi h+\tfrac12\log\{4(\sin^2\pi t+\sinh^2\pi h)\},\\
 I_h(s,x)&=\int_0^s L_h(x+t)\,dt,\\
 \lambda(s)&=\Re S(s),\\
 R_\epsilon(s,z)&=\lambda(s)+I_h(s,x)-\epsilon J(s).
\end{split}                                                   \tag{4}
\]
Here \(J(s)=\int_0^s\log(2\sin\pi t)\,dt\) on \(0<s<1\),
and \(S(s)=F(s,u_c(s))\) is the original endpoint action from the
[full real-index theorem](research_complete_boundary_full_index_interval.md).
That theorem applies on every compact subinterval of \((0,1)\),
including indices above \(1/2\). No complex-index packet outside
its proved domains is used in the real-row estimates below.

On such a compact interval the full endpoint packet, the uniform
factorial estimate, and the zero-safe product bound give, for every
\(\eta>0\), a fixed ordinary-color neighborhood on which
\[
 |B_{i,N}^{\epsilon}(w,z)|
       \le C N^A e^{N(R_\epsilon(i/N,z)+\eta)}.             \tag{5}
\]
The constants are uniform for \(z\in T_{3+\epsilon}\). The product
bound is valid through \(s+x=1\): lower clipping of \(L_h\) at
\(-\log N\) gives total variation \(O(\log N)\) and an integral
error \(O(N^{-1})\), uniformly in \(h\). This is the argument in
[the zero-safe product lemma](research_mixed_half_angle_seam_source.md),
Section 3. Thus (5) retains every revived Pochhammer row.
All bounds below include both parities and every fixed ordinary jet.

## 2. An exact derivative identity above one half

For \(1/2\le s<1\), write the original square root as
\[
 \sqrt{1-2e^{2\pi i s}}=a+ib,\qquad
 q=\sqrt{1-b^2},\qquad A=1+q+b.
                                                               \tag{6}
\]
The continued branch has \(a>0\), \(0\le b<1\), and
\(a^2+b^2=1+2q\), as proved in the full real-index theorem.
Consequently \(q^2+b^2=1\), \(q,b\ge0\), and \(A\ge2\).

**Lemma 1.** On this interval,
\[
 \lambda'(s)-J'(s)=-2\log A\le-\log4,\qquad
                         \lambda'(s)\le-\log2.             \tag{7}
\]

*Proof.* Put \(t=\tan(\pi u_c)=(a+i(1+b))/2\).
The original equation \(F_u=0\), not merely an unmarked
algebraic root, gives
\[
 e^{S'(s)}=e^{i\pi s}\frac{1+it}{2t^3}.
\]
Let \(Q=a^2+b^2\). Taking squared moduli yields
\[
 e^{2\lambda'}
 =\frac{4(Q+1-2b)}{(Q+1+2b)^3}
 =\frac{2q(1+q)}{(1+q+b)^4}.
                                                               \tag{8}
\]
The real part of \(1-2e^{2\pi is}=(a+ib)^2\) also gives
\(4\sin^2\pi s=2q(1+q)\). Dividing (8) by this identity
proves (7); \(J'(s)\le\log2\) gives its second assertion.
All denominators are nonzero for \(s<1\). \(\square\)

**Lemma 2.** For \(z\in T_{3+\epsilon}\), the function
\(s\mapsto R_\epsilon(s,z)\) is strictly decreasing on
\([.49,1)\). Wherever its derivative is finite,
\[
                         \partial_sR_\epsilon<-1/10.      \tag{9}
\]

*Proof.* First let \(s\ge1/2\). For type four, \(h<0\), so
\(|1-e^{-2\pi i(s+z)}|\le2\). Equation (7) gives
\(\partial_sR_1\le-\log2\).

For type three, \(x\in[.278,.391]\). On
\(1/2\le s\le1\),
\[
 \sin(\pi s)|\sin\pi(s+x)|\le\cos(.278\pi).
\]
Before \(s+x=1\), the positive product decreases from its value
\(\cos\pi x\) at \(s=1/2\). After that point its magnitude is at
most \((1-\cos\pi x)/2\le1/2<\cos(.278\pi)\).
Combining this fact with (7) gives
\[
 e^{\partial_sR_0}
 \le e^{.021\pi}
       \sqrt{\cos^2(.278\pi)+\sinh^2(.072\pi)}
 <3/4.
                                                               \tag{10}
\]

It remains to bridge \([.49,.5]\); (7) is not extrapolated to it.
On \(0<s<1/2\) the original endpoint saddle satisfies
\(0<\Re u_c<s<1/2\). The negative real Hessian of \(F(s,u)\)
is the positive sum
\[
 \pi\Re(2\tan\pi u+3\cot\pi u)\,du^2
             +\pi\Re\cot\pi(s-u)\,(ds-du)^2.
\]
The exact complex Schur complement therefore gives
\(\lambda''(s)<0\). Direct outward scalar evaluation on the
original explicit branch gives
\[
                 \lambda'(.49)<-3/5,\qquad J'(.49)>3/5.
                                                               \tag{11}
\]
For type three and \(s\in[.49,.5]\), one has
\(.768\le s+x\le.891\), hence
\[
 |1-e^{-2\pi i(s+z)}|
 \le 2e^{.021\pi}
        \sqrt{\sin^2(.768\pi)+\sinh^2(.072\pi)}
 <e^{1/2}.
                                                               \tag{12}
\]
Equations (11)--(12) give (9). For type four, use
\(L_h(s+x)\le\log2<7/10\),
\(\lambda'(s)<-3/5\), and \(J'(s)>3/5\); its derivative
is less than \(-1/2\). The bounds (10)--(12) are checked as
scalar inequalities, not by a parameter grid. At a real
Pochhammer zero, its logarithmic derivative has an integrable
singularity; integration on both sides and continuity of \(I_h\)
give the same monotonic conclusion. \(\square\)

There is also a lower-tail consequence for both types. On
\(0<s\le.27\), the same Schur concavity and two scalar bounds give
\[
 \lambda'(s)\ge\lambda'(.27)>27/50,\qquad
                  J'(s)\le J'(.27)<41/100.                \tag{12a}
\]
For either outgoing rectangle, \(.246\le x+s\le.661\).
The cosine of \(2\pi(x+s)\) is less than \(1/16\), by its
two endpoint values and its single interior minimum. Put
\(v=e^{-2\pi|h|}>1/2\); the last inequality follows from
\(|h|\le.108\). Then
\[
 |1-ve^{-2\pi i(x+s)}|^2
       =1+v\{v-2\cos(2\pi(x+s))\}>1.
\]
The actual logarithm \(L_h(x+s)\) is the logarithm of this
modulus plus \(2\pi h_+\), so it is positive. Thus
\[
              \partial_sR_\epsilon(s,z)>13/100
                         \quad(0<s\le.27).                \tag{12b}
\]
This conclusion uses the actual smoothed product, not its zero-height
value, and applies to both \(\epsilon=0,1\).

## 3. The actual endpoint rows, without a packet extrapolation

The compact-interval theorem cannot be used uniformly as \(s\to0\)
or \(s\to1\). Use instead the literal finite coefficient in (1).
For a physical row \(s=i/N\), all its endpoint terms have
\(0\le u=l/N\le s\). The original uniform product bounds give
the upper entropy
\[
 B(s,u)=\mathcal V(u)-J(u)-J(s-u),\qquad
 \mathcal V(u)=2\int_0^u\log(2|\cos\pi t|)\,dt-2J(u).
                                                               \tag{13}
\]
At the complete color this bounds every original term by a
polynomial prefactor; for a fixed small ordinary-color disk add
an arbitrarily small \(\eta\). This follows from the zero-safe
Newton-product bound and does not divide by an odd-level zero.

**Lemma 3.** Uniformly on (3), for every \(\eta>0\) and a
sufficiently small fixed ordinary-color neighborhood,
\[
\begin{array}{ll}
 |B_{i,N}^{\epsilon}(w,z)|\le C N^A e^{N(1/4+\eta)},
                                     &0\le i/N\le.01,\\
 |B_{i,N}^{\epsilon}(w,z)|\le C N^A e^{N(3/4+\eta)},
                                     &.99\le i/N<1.
\end{array}                                                     \tag{14}
\]

*Proof.* For \(s\le.01\), \(J\) is decreasing on \([0,s]\),
and
\[
 \mathcal V(u)\le2u\log2-2J(u),\qquad
 J(s)\ge s\log(4s)-s .
                                                               \tag{15}
\]
The latter follows from \(\sin\pi t\ge2t\) on \([0,1/2]\).
Thus (13), the extra reciprocal \(P_i^\epsilon\), and
\(|p_i(X)|\le(1+e^{.042\pi})^i<(9/4)^i\) give rate at most
\[
             2s\log2-5J(s)+s\log(9/4)<1/4.
                                                               \tag{16}
\]
For example use \(s\le.01\), \(\log25<7/2\),
\(\log2<7/10\), and \(\log(9/4)<1\); the resulting ceiling
is \(249/1000\). The limit at \(s=0\) is included.

For \(s=1-\delta\), \(0\le\delta\le.01\), reflection gives
\[
 B(s,u)=\mathcal V(u)+J(u+\delta)-J(u)
            \le\max_{[0,1]}\mathcal V+\delta\log2.
                                                               \tag{17}
\]
Here \(J'\le\log2\). Moreover
\[
 \max\mathcal V=-4J(1/4)=2G/\pi<3/5,                       \tag{18}
\]
where \(G=\sum_{k\ge0}(-1)^k/(2k+1)^2\). On the lower
half, \(\mathcal V'=2\log\cot\pi u\), so its maximum is at
\(1/4\); on the upper half use
\(\mathcal V(1-u)=-\mathcal V(u)\).
For the last strict inequality it suffices that
\(G<1-1/9+1/25=209/225\) and \(\pi>31/10\).

Both attached rectangles lie in
\([.24,.40]+i\{h:h\le.021\}\). The exact full product gives
\[
 p_i(X)=\frac{1-X^N}
               {\prod_{k=i+1}^{N}(1-r^kX)}.
                                                               \tag{19}
\]
Each denominator angle has real argument modulo one in
\([.23,.40]\). If its cosine is nonpositive, its modulus is
at least one for every radial modulus. Otherwise minimization
over that radial modulus bounds it below by
\(\sin(.46\pi)>.99\). Thus no denominator in (19) vanishes,
and
\[
              |p_i(X)|\le2e^{2\pi Nh_+}(100/99)^{N-i}.
                                                               \tag{20}
\]
This exact estimate includes all revived rows beyond the physical
Pochhammer cutoff. Since \(J(s)\ge0\) for \(s\ge.99\),
the remaining reciprocal \(P_i^\epsilon\) has nonpositive rate.
Combining (17)--(20) yields the uniform ceiling
\[
       \frac35+\frac{21\pi}{500}
          +\frac1{100}\log(200/99)<\frac34.                 \tag{21}
\]
Uniform finite-product errors and the at most \(N\) endpoint
summands change only the polynomial prefactor. This proves (14).
\(\square\)

## 4. The remaining scalar comparisons

**Theorem 4.** For each \(\eta>0\), uniformly on (3) and on a
fixed sufficiently small ordinary-color neighborhood,
\[
\begin{split}
 \sum_{i/N\ge.49}|B_{i,N}^{\epsilon}(w,z)|
 &\le C N^A
     \exp N\{\max(R_\epsilon(.49,z),3/4)+\eta\},\\
 \sum_{i/N\le.27}|B_{i,N}^{\epsilon}(w,z)|
 &\le C N^A
     \exp N\{\max(R_\epsilon(.27,z),1/4)
                    +\eta\}.
\end{split}                                                     \tag{22}
\]
For the first estimate, apply (5) on \([.49,.99]\) and
Lemma 2, then add the literal endpoint bound. The second uses
(5) on \([.01,.27]\), (12b), and Lemma 3. The sum of at most \(N\)
rows is absorbed in the same kind of polynomial factor.

Let \(M_\epsilon(z)\) denote the real part of the proposed
selected cap action, retaining its actual correlated endpoint
critical point. In particular it is not a value selected by
independent optimization over the rectangles (3). A uniform
upper-tail gap follows from the explicit condition
\[
 M_\epsilon(z)>
              \max\{R_\epsilon(.49,z),3/4\}+\delta
                                                               \tag{23}
\]
for a fixed \(\delta>0\); the lower tail has the analogous
condition displayed in (22). These comparisons have not been
proved here. Outer horizontal aliases and vertical currents retain their
own hypotheses. Thus (22) is a source estimate useful in an outer
contour proof, not a claim of open-word noncancellation.
