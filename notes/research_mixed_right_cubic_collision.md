# A cubic collision and a marked-phase change beyond the half-period

Research proof, 5 November 2026. Two fixed calculations describe obstacles
to extending the same simple conditional saddle through the whole right
half. The first identifies a collision of the algebraic continuation of
the original root. The second identifies an exact logarithmic lift change.
Neither calculation asserts failure of a finite conditional sum, cancellation
of its leading term, or dominance of a particular contour current.

## 1. Original polynomial and the continuation being followed

For real outer angles \(a,b\in(0,1)\), put
\(p=\cot\pi a\), \(q=\cot\pi b\), and \(S=\cot\pi s\).
The type-four exponentiated critical equation is
\[
 F(S;p,q)=(S+i)(S+p)(S+q)-2i(p-i)(q+i)=0.                 \tag{1}
\]
At \(p>0,q=0\), the
[closed cotangent theorem](research_mixed_closed_cotangent_roots.md)
selects the simple original zero-lift root in
\(\Re S>0,\ |\Im S|<1\). Below we continue this *algebraic*
root as real \(q\) decreases. Outside the original factorial strips,
the polynomial alone does not specify the contributing logarithmic lift.

There is no root of (1) on the imaginary axis for \(p>0,q\le0\).
Indeed, at \(S=iv\),
\[
 \Re F=p(2-v^2-v)-q(2+v^2+v),\qquad
 \Im F=(v-1)pq-v^2(v+1)-2.                               \tag{2}
\]
Since \(2+v^2+v\ge7/4\), the first equation with \(q<0\)
forces \(v>1\) or \(v<-2\). In the first case the second
expression is negative. In the second it is positive: its first term
is positive and \(-v^2(v+1)-2>2\). If \(q=0\), the first
equation permits only \(v=1,-2\), with imaginary values \(-4,2\).
Consequently a simple continuation from the selected root stays in the
right half-plane. On a bounded parameter interval no root escapes to
infinity, since (1) is monic with bounded coefficients.

## 2. An exact real-parameter double root

Let \(D=\operatorname{disc}_S F\), with real and imaginary parts
\(D_R,D_I\). Exact elimination gives
\[
 \operatorname{Res}_q(D_R,D_I)=-256(p^2+1)^5W(p),           \tag{3}
\]
where
\[
\begin{aligned}
 W(p)={}&81p^{16}+34412p^{14}+4632744p^{12}+276067068p^{10}\\
 &+7895210226p^8+107074960628p^6+551742302000p^4\\
 &+65754674660p^2-389141071067.
\end{aligned}
\]
Every coefficient of \(W'\) is positive. Exact rational signs isolate
its unique positive zero \(p_0\) in
\[
 0.85614860821687362<p_0<0.85614860821687364.               \tag{4}
\]
The penultimate subresultant is \(16(p^2+1)^3(A(p)q+B(p))\), where
\[
\begin{aligned}
 A(p)={}&24p^{12}+11849p^{10}+1152259p^8+36800794p^6\\
       &+392808686p^4+110330813p^2-252846825,\\
 B(p)={}&-1271p^{11}-125181p^9-2725502p^7-5163890p^5\\
       &+125665653p^3+134257263p.
\end{aligned}
\]
The interval (4) excludes \(A=0\). Substituting \(q=-B/A\)
in both discriminant parts gives numerators divisible by \(W\).
Thus \(q_0=-B(p_0)/A(p_0)\) is a real collision parameter.
Conversely every common zero of \(D_R,D_I\) at \(p=p_0\)
must annul this nonzero linear subresultant, so \(q_0\) is the
only real collision on this line.

For a monic cubic \(z^3+cz^2+dz+e\), put
\(K=c^2-3d\) and \(r=(9e-cd)/(2K)\). Direct identities are
\[
\begin{aligned}
 3r^2+2cr+d&=-\frac{9\operatorname{disc}}{4K^2},\\
 r^3+cr^2+dr+e
 &=-\frac{(2c^3-9cd+27e)\operatorname{disc}}{8K^3}.
\end{aligned}                                             \tag{5}
\]
Outward evaluation on (4) proves \(K\ne0\) and encloses
\[
\begin{aligned}
 q_0&\in(-3.534031,-3.534030),\\
 S_0&\in(2.199221,2.199223)+i(-.219473,-.219470),\\
 S_1&\in(-1.720563,-1.720560)+i(-.561059,-.561055).
\end{aligned}                                             \tag{6}
\]
Here \(S_0\) is the double root and \(S_1=-c-2S_0\)
is the simple third root. In outer-angle coordinates,
\(a_0\approx.2746197826\), \(b_0\approx.9122247201\).

**Proposition 1.** The algebraic continuation of the original selected
root at \((p,q)=(p_0,0)\) reaches the double root \(S_0\) as
\(q\downarrow q_0\).

There is no earlier discriminant zero by (3) and its linear
subresultant. Equation (2) keeps the selected continuation in
\(\Re S>0\). Its bounded limit must be a root at \(q_0\);
(6) leaves only the double root in that half-plane. In particular,
this same algebraic branch cannot remain simple on the whole path.
More explicitly, the local exponentiated gradient satisfies
\(e^{Q_s}-1=F(S;p,q)/(2i(p-i)(q+i))\). Its denominators are
nonzero here, and \(dS/ds=-\pi(1+S^2)\ne0\). Hence a
logarithmic lift made stationary at the double root has \(Q_{ss}=0\);
an ordinary nondegenerate Gaussian formula cannot hold there.
This does not identify its contributing contour current after a
factorial wall, or rule out a uniform expansion that treats colliding
saddles together.

## 3. A separate exact lift-change point

Fix \(p=1\) and decrease \(q\) from zero to \(-4\). Since
\(W(1)>0\), (3) excludes every real discriminant zero on this
line. The selected root at \(q=0\) is \(S=(1+i)t\), where
\[
 2t^3+2t^2+t-2=0,\qquad 3/5<t<7/10.                     \tag{7}
\]
Its imaginary part is initially positive. At \(q=-4\), three
disjoint rational disks of radius \(10^{-4}\), centered at
\[
 -1.8470906811-.6240183015i,\quad
 3.2434650668-.3352062951i,\quad
 1.6036256143-.0407754034i,
\]
contain exactly one root each and all lie below the real axis. The
checker verifies each disk by the strict Rouché inequality
\(r|F'(c)|>|F(c)|+r^2|3c+(p+q+i)|+r^3\).

At a positive real root \(S=u\), subtracting \(u\Im F\)
from \(\Re F\) gives \(2[u(q+1)+1-q]=0\). The case
\(u=1\) is impossible; otherwise \(q=(u+1)/(1-u)\), and
the remaining equation is \(u^2-3=0\). Thus the selected
right-half-plane continuation must pass through
\[
 p=1,\quad q=-2-\sqrt3,\quad S=\sqrt3,
 \qquad a=1/4,\quad b=11/12,\quad s=1/6.                 \tag{8}
\]
This is its only real-root crossing on that path, hence its first
height-zero crossing. It is not asserted to be the first factorial-wall
crossing.

Write the lower periodic primitive as
\(g_-(z)=(\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6)/(2\pi i)\)
below the real axis. At (8), the lower boundary phase
\[
 Q_{1,-}(s)=g_-(s+a)+g_-(s+b)-3g_-(s)+2\pi ias           \tag{9}
\]
has derivative zero. The real part of its derivative follows from
\(4\sin(5\pi/12)\sin(\pi/12)=1\); the imaginary part is
\(\pi/12+5\pi/12-3\pi/3+\pi/2=0\).
The [marked upper continuation](research_mixed_all_real_conditional_packet.md)
satisfies \(g_+'(z+1)=g_+'(z)-2\pi i\). Since
\(s+b=13/12\), while the other arguments are in \((0,1)\),
\[
              Q_{1,+}'(s)=-2\pi i.                       \tag{10}
\]
The same polynomial root is therefore stationary for
\(Q_{1,+}(s)+2\pi is\), not for the marked upper zero mode.

The [exact factorial continuation](research_lower_half_factorial_continuation.md)
retains the finite multiplier
\[
 P_N(N(s+b))=
 (1-e^{-2\pi iN(s+b-1)})P_N(N(s+b-1)).                  \tag{11}
\]
For \(N\) divisible by 12, both outer indices are physical integers.
In the canonical row
\(e^{2\pi iNa s}P_N(N(s+a))P_N(N(s+b))/P_N(Ns)^3\),
the numerator already vanishes whenever
\(j=Ns\ge N/12\), whereas its denominator is nonzero for
\(0\le j<N\). The index \(j=N/6\) of (8) is therefore
an exactly zero physical row. This is compatible with a nonzero
coherent sum: neither an individual row nor the polynomial critical
equation determines the full residue integral. Both components of
(11), the original cotangent aliases, and their contour currents
must be kept in any continuation argument.

## Reproduction and scope

    python3 experiments/check_mixed_right_cubic_collision.py --precision 320

The checker validates exact elimination identities and rational signs,
outward double-root bounds, and the three fixed Rouché disks. It binds
the original root and marked-factorial inputs. The monic continuation
and sign arguments are the written proof above. The
[fixed-witness archive](../repro/diagnostics/2026-11-05-right-cubic-collision/README.md)
contains no parameter search or temporary-file dependency.

What remains open here is a complete finite-source estimate beyond the
proved half-period neighborhoods, including the correct logarithmic
lifts and all currents. No finite-source or volume-asymptotic
counterexample is claimed.
