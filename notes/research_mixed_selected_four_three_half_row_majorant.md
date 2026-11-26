# Explicit scalar tests for the selected ordinary half row

Research deduction, 6 November 2026. The ordinary half-row phase
separates exactly in the outgoing coordinate. Its real maximum with
the original outgoing tangent has a closed clipped formula.
Quantitative concavity then removes the remaining real targets from
the cap-main and two cap-cut half-row comparisons. The resulting six
scalar upper bounds depend only on the same actual complex endpoint
parameter as the central comparison.

Their uniform signs are not proved here. In particular the old small
half-row gap is not assumed to pay a macroscopic selected-height
change. No root, source sum, interval cover, or old certificate is
evaluated or replayed.

## 1. The exact half-row separation

Retain the actual first-four/next-three reference and the notation
\(\Psi,Q,M,p,\ell_b,A_0,A_L,A_R,B_R,W_\sigma\) of
[the finite-source reduction](research_mixed_selected_four_three_finite_reduction.md).
Thus \(H=7/625\), \(z=y+iH\), \(b=v+ih_b\),
\(y,v\in P=[.22,.45]\), and \(-.065<h_b<.068\).
The original reference is
\((e_*,s_*;z_*,b_*)\), with
\[
 z_*=a+ic,\quad b_*=v_*+ih_b,\qquad
 p=g'(s_*+b_*)-g'(b_*).
\tag{1}
\]
All these quantities stay correlated; in particular \(p\) is not
an independent parameter.

Define the holomorphic function
\[
                         q(w)=g(w+1/2)-g(w).
\tag{2}
\]
Since \(\Re g(1/2)=J(1/2)=0\), the literal ordinary half row
has the exact real phase
\[
 B_R(y,v)=\Re q(y+iH)+\Re q(v+ih_b)-\pi H.
\tag{3}
\]
This follows from
\(Q(1/2;z,b)=q(z)+q(b)+i\pi z-2g(1/2)\).
The \(-\pi H\) term is the original first chirp, and no
endpoint or logarithmic constant has been suppressed.

The derivatives are
\[
 q'(w)=\log\frac{1+e^{-2\pi iw}}{1-e^{-2\pi iw}},
 \qquad q''(w)=-\frac{2\pi}{\sin(2\pi w)}.
\tag{4}
\]
The quotient notation for \(q'\) means the difference of the two
original logarithms. We use its real part below, so there is no
new logarithmic lift. On \(0<\Re w<1/2\),
\(\Re(1/\sin(2\pi w))>0\); hence every horizontal restriction
of \(\Re q\) is strictly concave.

## 2. The outgoing target is maximized exactly

Put \(p_R=\Re p\), \(r_b=e^{2\pi h_b}\), and
\[
 \zeta_b=\frac{r_b+r_b^{-1}}2\tanh p_R,\qquad
 \widehat v=\frac1{2\pi}\arccos
 \operatorname{clip}\bigl(\zeta_b,\cos(.9\pi),\cos(.44\pi)\bigr).
\tag{5}
\]
Here \(\operatorname{clip}(t,l,u)=\min(u,\max(l,t))\).
The argument of \(\arccos\) lies in \((-1,1)\), even when
\(\zeta_b\) does not. Define the calibrated outgoing maximum
\[
 \mathcal O_*=\Re q(\widehat v+ih_b)-p_R(\widehat v-v_*).
\tag{6}
\]

**Lemma 1.** The exact identity is
\[
 \mathcal O_*=
 \max_{v\in P}\{\Re q(v+ih_b)-\ell_b(v)\}.
\tag{7}
\]

Indeed the derivative before subtracting \(p_R\) is
\[
 \frac12\log
 \frac{1+r_b^2+2r_b\cos(2\pi v)}
      {1+r_b^2-2r_b\cos(2\pi v)}.
\tag{8}
\]
It strictly decreases on \(P\), by (4). Its equation with
\(p_R\) is exactly
\(\cos(2\pi v)=\zeta_b\); clipping the decreasing cosine
gives the correct maximizing endpoint when no interior solution
exists. This includes equality at either endpoint.

No derivative of a moving critical point is involved. Moreover (5)
can be formed directly from the rational reference exponentials
\(S_*=e^{-2\pi is_*}\), \(B_*=e^{-2\pi ib_*}\):
\[
 e^{2p_R}=\frac{|1-S_*B_*|^2}{|1-B_*|^2},
 \qquad r_b=|B_*|.
\tag{9}
\]
Thus the outgoing optimization introduces no free reference slope,
root solve, or target grid.

## 3. Quantitative concavity for the remaining targets

Write \(\nu=1\) for the factorial alternative and \(\nu=0\)
for the forced alternative. On the private main line define
\[
 F_\nu(x,y)=
 \Re\Psi(x+ih_e,y+iH)+\Re q(y+iH)
            -\pi H-\nu\Re g(y+iH)-2\nu\pi H.
\tag{10}
\]
At a real cap cut \(e_0\in\{.27,.49\}\), use the
one-variable function \(F_{\nu,e_0}(y)\) given by the same
formula with \(x+ih_e=e_0\).
By (3), these are exactly the incoming parts of the specified
joint profiles, with their full Fourier alternative.

**Lemma 2.** On \([.3,.4]\times P\),
\[
 -\nabla^2 F_\nu\succ
 \begin{cases}
 \operatorname{diag}(1,7),&\nu=1,\\
 \operatorname{diag}(1,33/5),&\nu=0.
 \end{cases}
\tag{11}
\]
At either real cap cut, on all \(P\),
\[
 -F_{\nu,e_0}''>
 \begin{cases}69/10,&\nu=1,\\13/2,&\nu=0.\end{cases}
\tag{12}
\]

*Proof.* The original cap Hessian has the exact decomposition
\[
 -\pi^{-1}\Re\Psi''=
 \operatorname{diag}(\sigma+u_e,u_z)
          -C\begin{pmatrix}1&1\\1&1\end{pmatrix},
\quad
 \sigma=-\Re S''/\pi>1/43,
\tag{13}
\]
where \(u_e=\Re\cot\pi e\), \(u_z=\Re\cot\pi z\),
and \(C=\Re\cot\pi(e+z)\).
The bounds and the canonical Schur inequality for \(\sigma\)
are from [the cap phase theorem](research_mixed_first_cap_plateau_phase.md).
On the main-line target rectangle, \(.52\le x+y\le.85\),
so \(C\le0\). Also \(u_z>9/70\).
For \(x\in[.3,.4]\), \(|h_e|<.051\), one has
\[
 u_e\ge
 \frac{\sin(\pi/5)}{\cosh(.102\pi)+\cos(\pi/5)}
 >\frac{7/12}{16/15+5/6}
 =\frac{35}{114}>\frac3{10}.
\tag{14}
\]
The real cotangent decreases in \(x\) on this interval.
The elementary estimates in (14) follow from the sine cubic,
the positive cosh series, and
\(\cos(\pi/5)=(1+\sqrt5)/4<5/6\).
In particular \(\pi(1/43+3/10)>1\).

There is a stronger curvature contribution from \(q\). Put
\(a_y=\sin(2\pi y)>3/10\) and \(C_H=\cosh(2\pi H)<101/100\).
Then
\[
 \Re\frac1{\sin(2\pi(y+iH))}
 =\frac{C_Ha_y}{a_y^2+C_H^2-1}>\frac{100}{101}.
\tag{15}
\]
For fixed \(a_y\le1\) this expression decreases with \(C_H\).
At \(C_H=101/100\), its dependence on \(a_y\in[3/10,1]\)
has only an interior maximum. At the endpoints its values are
\(1010/367\) and \(100/101\), respectively.
The estimate \(C_H<101/100\) follows from \(2\pi H<44/625\)
and the positive cosh series. Thus
\(-\Re q''>200\pi/101\).
Adding this contribution and, for \(\nu=1\), the additional
\(u_z\pi\), to (13) proves (11), since
\[
 \pi(9/70+200/101)>33/5,\qquad
 \pi(18/70+200/101)>7.
\tag{16}
\]
Both rational comparisons follow from \(\pi>157/50\).

At either real cut, \(C\le1/30\): it is nonpositive except
possibly at \(e_0=.27,\ y<.23\), where the sum is at least
\(.49\) and \(C\le\cot(.49\pi)<1/30\).
Consequently \(u_z-C>9/70-1/30=2/21\). The one-variable
versions of (13)--(15) give (12), using
\[
 \pi(2/21+200/101)>13/2,\qquad
 \pi(2/21+9/70+200/101)>69/10.
\tag{17}
\]
This proves every claimed bound on the full target intervals.
\(\square\)

For the main profile, restricting its maximum to
\(x\in[.3,.4]\) is legitimate for both alternatives. The original
[private upper barrier](research_mixed_selected_boundary_optimizer_bounds.md),
Proposition 1, and
[private lower barrier](research_mixed_selected_boundary_height_envelope.md),
Proposition 7, use only the cap's private derivative and the fixed
\(z\)-height range. Neither the ordinary half row, the outgoing
tangent, nor either Fourier alternative depends on \(e\).
Their proofs therefore exclude \(x\le.3\) and \(x\ge.4\) here
as well. This does not claim those barriers at the different heights
of the cap aliases, or move either real cap cut.

## 4. Six explicit reference-only majorants

For an interval \(l\le0\le u\), define the exact quadratic gain
\[
 \Gamma_\mu(p;l,u)=p\,t-\frac\mu2t^2,\qquad
 t=\operatorname{clip}(p/\mu,l,u).
\tag{18}
\]
It is the maximum of \(ph-\mu h^2/2\) over \(h\in[l,u]\).
This formula keeps maxima at target endpoints rather than replacing
them by unconstrained gains.

Use \(z_H^*=a+iH\), \(E_*=e^{-2\pi ie_*}\),
\(Z_*=e^{-2\pi iz_*}\), and
\(\lambda=e^{2\pi(H-c)}\). The two main-line derivatives at
the trial \((e_{*,R},a)\) are exactly
\[
 \begin{split}
 A&=\log\left|\frac{1-\lambda E_*Z_*}{1-E_*Z_*}\right|,\\
 P_\nu&=\log\left|
 \frac{(1-\lambda E_*Z_*)(1+\lambda Z_*)}
                      {(1-\lambda Z_*)^{2+\nu}}\right|.
 \end{split}
\tag{19}
\]
The first identity uses the original private equation
\(\Psi_e(e_*,z_*)=0\); the original chirps are already
included in \(\Psi\) and in (3).
Let \(\mu_1=7,\ \mu_0=33/5\), and define
\[
 \begin{split}
 \mathcal H_{0,\nu}={}&
 \Re\Psi(e_*,z_H^*)+\Re q(z_H^*)-\pi H
                   +W_\nu(a)+\mathcal O_*-M\\
 &+\Gamma_1(A;\ .3-e_{*,R},\ .4-e_{*,R})\\
 &+\Gamma_{\mu_\nu}(P_\nu;\ .22-a,\ .45-a),
 \qquad W_\nu(a)=-\nu\Re g(z_H^*)-2\nu\pi H.
 \end{split}
\tag{20}
\]
All trial coordinates lie in their proved target rectangles.
The private endpoint action cancels from the first line against
its occurrence in \(M\). Explicitly, that first line equals
\[
 \begin{split}
 &\Re\{g(e_*+z_H^*)-g(e_*+z_*)-g(z_H^*)+g(z_*)\}\\
 &\quad+\Re q(z_H^*)-\pi H+W_\nu(a)+\mathcal O_*
                    -\Re Q(s_*;z_*,b_*)+\Re g(z_*).
 \end{split}
\tag{21}
\]
Thus the main-profile test needs no evaluation of a private critical
action at a moving target.

For a cut \(e_0=.27\) or \(.49\), let \(E_0=e^{-2\pi ie_0}\)
and set
\[
 \begin{split}
 P_{\nu,e_0}&=\log\left|
 \frac{(1-\lambda E_0Z_*)(1+\lambda Z_*)}
                         {(1-\lambda Z_*)^{2+\nu}}\right|,\\
 \mathcal H_{e_0,\nu}&=
 \Re\Psi(e_0,z_H^*)+\Re q(z_H^*)-\pi H+W_\nu(a)
                         +\mathcal O_*-M\\
 &\qquad+
 \Gamma_{\widehat\mu_\nu}(P_{\nu,e_0};\ .22-a,\ .45-a),
 \qquad \widehat\mu_1=69/10,\quad\widehat\mu_0=13/2.
 \end{split}
\tag{22}
\]
The constants \(S(.27),S(.49)\) and the actual \(S(e_*)\)
in this formula are the original canonical actions, not new roots
or independently chosen branches.

**Proposition 3.** With \(i=0,L,R\), corresponding respectively
to \(\mathcal H_{0,\nu},\mathcal H_{.27,\nu},\mathcal H_{.49,\nu}\),
\[
 \sup_{y,v\in P}
 \{A_i(y)+B_R(y,v)+W_\nu(y)-M-\ell_b(v)\}
                         \le\mathcal H_{i,\nu}.
\tag{23}
\]

*Proof.* First apply the exact outgoing maximization (7).
For \(i=0\), the private barriers reduce the remaining maximum to
the rectangle of (11). Taylor's integral formula with the diagonal
Hessian lower bound gives an upper quadratic about
\((e_{*,R},a)\). Its two gradients are (19).
Maximizing that upper quadratic independently in the two real
displacements gives precisely the two clipped gains in (20).
For a cut, (12) gives the corresponding one-variable Taylor
inequality about \(y=a\); its derivative is (22).
This proves (23), including every possible endpoint maximum.
\(\square\)

Every actual input to (20)--(22) is determined by the one complex
endpoint coordinate \(U=e^{2\pi iu_*}\) and the original rational
maps \(E(U),Z(U),S(U),B(U)\) used in the
[central scalar proof](research_mixed_first_four_next_three_central_gap.md).
The canonical logarithms recover the actual coordinates, and all the
typed-disk, pair-sum, and next-external compatibility restrictions
remain necessary. In particular (23) does not replace that actual
family by independently varied increments or slopes.

A concrete sufficient next test is therefore
\[
 \max_{\substack{i\in\{0,.27,.49\}\\\nu\in\{0,1\}}}
                         \mathcal H_{i,\nu}(U)<-\delta
 \quad\text{on the admitted actual-reference family}
\tag{24}
\]
for some fixed \(\delta>0\).
It has only the two real reference parameters: all real integration
targets have been removed by (5) and (18). Its values consist of
original regular logarithms and primitives, clipped real functions,
and the explicit canonical endpoint action at fixed cuts or the
actual reference. Formula (24) has not been checked and no sign is
asserted. If it fails as an upper bound on a larger necessary
superset, that would not by itself refute any original profile.

The new proved ingredients are the exact outgoing maximum and the
quantitative, fully specified scalar bounds (20)--(23). They preserve
the outgoing tangent and both complete Fourier alternatives. They do
not prove the other real-cut profiles or whole selected-source
dominance.
