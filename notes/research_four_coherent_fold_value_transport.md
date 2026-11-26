# Anchored source transport reaches the central fold value

22 November 2026. Research note. Author-final. Earlier final notes and public
manuscripts remain unchanged.

The original four-coherent scalar has the positive ideal-cube rate
uniformly along its entire anchored half-grid up to the central fold.
No fixed distance from that fold is required. If the grid lands on
the fold, the estimate includes its actual value, without using the
singular boundary-equation row there.

An explicit sine factor removes the potentially shrinking first
difference. The resulting positive flux has a bounded total
correction, and converting back costs at most a polynomial factor.
No source, seam, or repeated-root coordinate is replaced.

## 1. The original source and the extended range

Let \(N\ge2\), \(d=N-1\), \(q=e^{\pi i/N}\), and \(Q=q^2\).
In the full centered basis put
\[
 U_a=\sum_{\ell=0}^d a^\ell f_\ell,\qquad
 \Phi_N(y,z;s,t)=\phi(U_yU_zU_sU_t).
 \tag{1}
\]
This is the original Frobenius contraction, including all internal
Hermite derivative coordinates and its original phases.

Fix a compact subset \(K\) of the three-parameter domain
\[
 b,c>0,\qquad S=b+c<1,\qquad
                         1-S<R<1-\max(b,c).
 \tag{2}
\]
Set \(\varepsilon=N^{-1}\) and
\[
 \begin{gathered}
 y=-e^{-2\pi ib},\quad z=-e^{-2\pi ic},\quad r=e^{-2\pi iR},\\
 h_j=(j+\tfrac12)\varepsilon,\quad k_j=R-h_j,\quad
 s_j=-q^{-1}Q^{-j},\quad t_j=-qrQ^j,\\
 \Phi_j=\Phi_N(y,z;s_j,t_j),\qquad
 \omega_N=e^{-\pi i d(S+R)} .
 \end{gathered}
 \tag{3}
\]
The allowed targets are all integers
\[
               J\ge0,\qquad 0<h_J\le R/2.
 \tag{4}
\]
Thus the target can be \(O(N^{-1})\) from the fold or exactly at it.
The entries \(-1,0\) initialize the same anchored orbit.

Use the actual source action
\[
 \begin{split}
 L(x)&=\int_0^x\log|2\sin\pi v|\,dv,\\
 m(x,y,u)&=L(x+y)+L(u)-L(x)-L(y)\\
         &\hspace{10mm}-L(u-x)-L(u-y)-L(x+y-u),
 \end{split}
 \tag{5}
\]
where \(L\) has its odd, one-periodic extension. Put
\[
 \begin{split}
 I_h&=(\max(b,c,1-R),\ \min(S,1-h,1-R+h)),\\
 \mathcal F(b,c,R,h)&=
  \max_{u\in I_h}\{m(b,c,u)+m(h,R-h,1-u)\}.
 \end{split}
 \tag{6}
\]
The [actual cube theorem](actual_newton_ideal_prism_and_associativity.md)
identifies \(\pi\mathcal F\) with the volume of its convex ideal cube.
This remains a strict cube at \(h=R/2\): all six external pair sums
are below one, and their total is \(S+R>1\). The fold is in the
boundary parametrization, not a degeneration of this ideal cube.

**Theorem.** There are constants \(C_K,N_K\) such that for every
\(N\ge N_K\), every \((b,c,R)\in K\), and every target (4),
\[
 \boxed{\quad
 \Phi_J=\omega_N P_{N,J},\qquad P_{N,J}>0,\qquad
 |\log P_{N,J}-N\mathcal F(b,c,R,h_J)|\le C_K\log N .
 \quad}
 \tag{7}
\]
The estimate is uniform even when \(h_J\) tends to zero or to the
fold at a level-dependent rate. Both parities and composite levels
are included. The normalized original closing of the two turned
products is \(\Phi_J/N^2\), and has the same rate.

## 2. Exact source initialization and the rows actually used

The [anchored-grid theorem](research_four_coherent_anchored_grid_volume.md)
supplies the exact common carrier in (3), the two original readouts,
and their calibrated asymptotics. Consequently
\[
 \begin{gathered}
 H_j=\omega_N^{-1}\Phi_j\in\mathbb R,\qquad
 H_0>0,\qquad \Delta_0:=H_0-H_{-1}>0,\\
 \log H_0=N M(b,c,R)+O_K(\log N),\qquad
 M(b,c,R)=m(b,c,1-R)>0,\\
 |H_{-1}|\le C_K/N,\qquad
 \Delta_0/H_0=1+O_K(e^{-c_KN}).
 \end{gathered}
 \tag{8}
\]
Only the compact parameters in (2) enter these bounds. Indeed the
entry \(0\) is an original three-input scalar at angles
\(b,c,R-1/(2N)\); these remain in a compact strict prism family.
The entry \(-1\) is its elementary socle readout.

For a fixed target \(J\), put
\[
 \delta_j=R-2h_j,\qquad
 \alpha_j=\sin\pi(R-2j\varepsilon)
           =\sin\pi(\delta_j+\varepsilon).
 \tag{9}
\]
For every row \(0\le j<J\),
\[
 \delta_j=\delta_J+2(J-j)\varepsilon\ge2\varepsilon,\qquad
 0<\delta_j-\varepsilon<\delta_j+\varepsilon\le R<1.
 \tag{10}
\]
Therefore every boundary row used in the proof is regular.
In particular
\(\alpha_{j+1}=\sin\pi(\delta_j-\varepsilon)>0\).
At the terminal point,
\[
                  c_K/N\le\alpha_J\le1,
 \tag{11}
\]
including \(\alpha_J=\sin(\pi/N)\) when \(\delta_J=0\).
No boundary equation is imposed at row \(J\).

Write the positive numerators of the sine-converted coefficients as
\[
 \begin{split}
 \mathcal B_j={}&
 \sin^2\pi(k_j+\varepsilon/2)
 \sin\pi(b+h_j-\varepsilon)\sin\pi(c+h_j-\varepsilon),\\
 \mathcal D_j={}&
 \sin^2\pi(h_j+\varepsilon/2)
 \sin\pi(b+k_j-\varepsilon)\sin\pi(c+k_j-\varepsilon).
 \end{split}
 \tag{12}
\]
Then the exact source recurrence, with
\(\Delta_j=H_j-H_{j-1}\), is
\[
 \begin{gathered}
 \Delta_{j+1}=\rho_j\Delta_j+
                         \frac{\Lambda_N}{\mathsf d_j}H_j,\\
 \mathsf b_j=\frac{\mathcal B_j}{\sin\pi\delta_j\,\alpha_j},
 \quad
 \mathsf d_j=\frac{\mathcal D_j}{\sin\pi\delta_j\,\alpha_{j+1}},
 \quad
 \rho_j=\mathsf b_j/\mathsf d_j,\\
 \Lambda_N=\sin(\pi/N)\sin\pi(S-\varepsilon).
 \end{gathered}
 \tag{13}
\]
All coefficients in these used rows are positive for large \(N\).
Uniformly there,
\[
       \mathcal B_j\ge c_K>0,\qquad
                         0<\Lambda_N\le C_K\varepsilon .
 \tag{14}
\]
For example \(k_j+\varepsilon/2\) stays between \(R/2\) and \(R\);
the other two arguments in \(\mathcal B_j\) stay in compact
subintervals of \((0,1)\). This proves (14) without bounding the
possibly large divided coefficients near the fold.

## 3. Removing the shrinking sine from the first difference

Set
\[
 q_j=\mathcal B_j/\mathcal D_j,\qquad
 E_j=\Delta_j/\alpha_j .
 \tag{15}
\]
The exact relation between the two transfer factors is
\[
             \rho_j=q_j\,\alpha_{j+1}/\alpha_j .
 \tag{16}
\]
Unlike \(\rho_j\), the factor \(q_j\) stays above one throughout
the used half-path. For a quantitative bound define
\[
 f_N(v)=\frac{\sin^2\pi v}
 {\sin\pi(b-3\varepsilon/2+v)\sin\pi(c-3\varepsilon/2+v)} .
 \tag{17}
\]
Then \(q_j=f_N(k_j+\varepsilon/2)/f_N(h_j+\varepsilon/2)\).
Its logarithmic derivative is the sum of two positive cotangent
differences. The identity
\(\cot x-\cot(x+a)=\sin a/[\sin x\sin(x+a)]\)
gives a lower bound \(c_K>0\), even when the first argument is
of order \(N^{-1}\). Since the two arguments differ by \(\delta_j\),
\[
                       q_j-1\ge c_K\delta_j .
 \tag{18}
\]
Here the shifted \(b,c\) are positive for large \(N\), and all
shifted arguments remain in \((0,1)\), by (2).

Dividing (13) by \(\alpha_{j+1}\) now gives
\[
 E_{j+1}=q_jE_j
       \left(1+\beta_j\frac{H_j}{E_j}\right),\qquad
 \beta_j=\frac{\Lambda_N\sin\pi\delta_j}{\mathcal B_j},
 \qquad 0<\beta_j\le C_K\varepsilon\delta_j .
 \tag{19}
\]
Starting with (8), induction proves
\(E_j,\Delta_j,H_j>0\) for every \(0\le j\le J\).
In particular \(E_{j+1}\ge q_jE_j\).

We next bound \(H_j/E_j\) without a fixed fold margin.
For every \(j<J\), (10) and (18) imply
\[
 \alpha_jE_j\le C_K\delta_jE_j
                         \le C_K(E_{j+1}-E_j).
 \tag{20}
\]
For a target \(1\le n\le J\), use
\[
 H_n=H_0+\sum_{j=1}^n\alpha_jE_j.
 \tag{21}
\]
Apply (20) up to \(n-1\), and bound the final term by \(E_n\).
Since \(E_n\ge E_0=\Delta_0/\sin\pi R\), (8) gives
\(H_n/E_n\le C_K\). Conversely \(H_n\ge\Delta_n=\alpha_nE_n\).
At \(n=0\) the analogous comparison follows directly from (8).
Thus, uniformly along the entire path,
\[
                    c_K/N\le H_n/E_n\le C_K .
 \tag{22}
\]
The lower bound uses \(\alpha_n\ge c_K/N\) for all \(n\le J\),
not a lower bound independent of \(N\).

By (19) and (22), the logarithmic correction to the product of
the \(q_j\)'s is at most \(C_K\varepsilon\sum_{j<J}\delta_j\),
which is bounded. Therefore
\[
 \log E_J=\log E_0+\sum_{j=0}^{J-1}\log q_j+O_K(1),\qquad
 \log H_J=\log H_0+\sum_{j=0}^{J-1}\log q_j+O_K(\log N).
 \tag{23}
\]
Equivalently, an explicit finite-level estimate is
\[
 \frac{c_K}{N}\prod_{j<J}q_j
       \le\frac{\Phi_J}{\Phi_0}
       \le C_K\prod_{j<J}q_j .
 \tag{24}
\]
The ratio is real and positive, with the original source carrier
retained. Empty sums and products cover \(J=0\).

## 4. The same geometric action, uniformly at the terminal fold

The product now contains no divided fold factor:
\[
 q_j=\frac{\sin^2\pi(R-j\varepsilon)}
              {\sin^2\pi((j+1)\varepsilon)}
 \frac{\sin\pi(b+(j-\tfrac12)\varepsilon)
       \sin\pi(c+(j-\tfrac12)\varepsilon)}
      {\sin\pi(b+R-(j+\tfrac32)\varepsilon)
       \sin\pi(c+R-(j+\tfrac32)\varepsilon)} .
 \tag{25}
\]
All its factors are smooth log-sine samples on fixed strict intervals,
apart from the explicit denominator at the initial endpoint.
The usual integral comparison for \(\log(J!)\), together with
\(\log\sin\pi v=\log v+\) a smooth function near zero, gives
uniformly up to \(h_J=R/2\),
\[
 \begin{split}
 \sum_{j<J}\log q_j
 &=N\int_0^{h_J}\log\rho_0(v)\,dv+O_K(\log N),\\
 \rho_0(v)&=
 \frac{\sin^2\pi(R-v)\sin\pi(b+v)\sin\pi(c+v)}
      {\sin^2\pi v\sin\pi(b+R-v)\sin\pi(c+R-v)} .
 \end{split}
 \tag{26}
\]
The bounded shifts cost \(O_K(1)\); changing \(J/N\) to \(h_J\)
costs at most \(O_K(\log N)\) after multiplication by \(N\).
There is no singularity at the upper endpoint:
\(\rho_0(R/2)=1\).

The anchored-grid proof identifies, on \(0<h<R/2\),
\[
 \mathcal F(b,c,R,h)
       =M(b,c,R)+\int_0^h\log\rho_0(v)\,dv .
 \tag{27}
\]
This identity extends to \(h=R/2\) by continuity. The actual cube
theorem applies there as well: its two prism actions still have a
unique strict stationary maximum. Combining (8), (23), and (26)--(27)
proves (7). No singular target row was used to obtain that value.

## 5. What has and has not been extended

This removes the fixed fold margin for actual values on the anchored
orbit. In particular every closest prefold grid point is covered,
and an exact central grid value is covered whenever it occurs.
The proof uses only the original finite boundary equation in regular
rows and its original two source anchors.

It does not estimate a derivative normal to the folded boundary
coordinate, nor does it apply the pole-cancelled target equation
to identify such a derivative. It does not prove transport to a
fixed postfold interval, use a reflected fractional orbit, or remove
the anchored-grid and initial pair-wall restrictions in (2)--(4).
The original scalar and its \(N^{-2}\) coherent normalization are
unchanged. No general Conway attachment or finite-exception
knot-volume theorem follows.

The complete direct proof sources are:

| Source | SHA-256 |
|---|---|
| [Anchored original-source transport, 418 lines](research_four_coherent_anchored_grid_volume.md) | d79b3f5bb0f2cb325214015cf9b4b15ca4ac8892ff5d1d42df794b89f7d2771d |
| [Actual prism and cube geometry, 377 lines](actual_newton_ideal_prism_and_associativity.md) | c29321805df39a49854665df1255db1ec7180397a5dd689f19289d61335871c9 |

Both whole texts were read at their matching pins. The flux change,
uniform bounds and terminal-value extension are proved above.
Only written mathematics and text operations were used.
