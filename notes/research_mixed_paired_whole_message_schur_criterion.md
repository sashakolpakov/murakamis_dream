# A whole-message criterion for iterating the original paired kernel

Research reduction, 7 November 2026. A local asymptotic for the
complete three-four kernel does not bound its action on an incoming
function outside that local chart. This note isolates a sufficient
weighted integral estimate which does propagate the whole message,
its local remainder, and its original phase and amplitude. The
estimate and the initial whole-message entrance are hypotheses,
not conclusions of the existing local entrance theorem. No new
function values or numerical signs are asserted.

## 1. The exact operator and a whole-period norm

Use the actual alternating reference \(x_0\), and write
\[
 K_N(z,y)=\mathcal K_{34,N}(x_0+z,x_0+y),\qquad
 (L_NG)(y)=N\int_\Gamma G(z)K_N(z,y)\,dz,
 \tag{1}
\]
where \(\Gamma=[-1/2,1/2]\) is one period at the original
height of \(x_0\). By the
[exact Fourier bridge](research_mixed_conditional_fourier_message_bridge.md),
this is attachment by the full original \(A_3A_4\). Both factors
in the integrand are antiperiodic at even levels, so their product
is periodic and (1) is unchanged. There is no discarded matrix
corner, conditional Fourier alternative, or closing scalar.

The proved
[whole-kernel theorem](research_mixed_contracted_pair_full_kernel.md)
supplies, on a fixed local bidisk,
\[
 K_N(z,y)=\kappa_N^3N^{-1/2}B(z,y)e^{N\psi(z,y)}
                                             (1+O(N^{-1})).
 \tag{2}
\]
The phase is the original calibrated paired phase. Here \(B\)
means this complete kernel's own nonzero coefficient, with its
specified four-index Gaussian root. Equality with a differently
chosen local-current coefficient is not assumed.

Take the invariant phase class \(S_h\), map \(h^+=\mathcal Gh\),
critical input \(\chi_h\), and exact action increment \(C(h)\)
of [the local basin](research_mixed_alternating_interface_local_entrance_basin.md).
Choose its disk \(D_R\) small enough for (2), and also require
\(0<R<\Im x_0/2\). Thus the physical period, this disk and
every permitted deformation have external exponentials in a
fixed compact subset of \(0<|X|<1\). Set
\(\Lambda=\Gamma\cup\overline D_R\). For each admitted \(h\),
choose a bounded real weight \(W_h\) on \(\Lambda\), agreeing
with \(\Re S_h\) on the disk, and with matching period-end
values. Its values on the rest of the period are additional data;
the local phase is not analytically continued there by notation.
For a finite Fourier message define
\[
                  \|G\|_{h,N}
       =\sup_{z\in\Lambda}|G(z)|e^{-NW_h(z)}.
 \tag{3}
\]

Allow a full-period contour \(\Gamma_{h,y}\) homologous to
\(\Gamma\), with its ends identified periodically. Any change
from \(\Gamma\) takes place inside \(D_R\), and the contour
stays in \(\Lambda\). For local \(y\), designate a short
central arc \(\gamma_{h,y}\) through \(\chi_h(y)\), with
uniform quadratic descent and endpoints a fixed positive distance
from that saddle. Accretivity and the strict interior-input
property permit this arc inside the local disk. Its connecting
pieces are retained in the rest of the full contour; no decay
on those pieces is inferred just from existence of the arc.
The complete finite integrand
is entire, so its integral is exactly (1). No old graph depending
on an eliminated variable is projected onto the retained contour.

## 2. A sufficient Schur bound, with exterior leakage separated

The missing operation-level condition is the following. There
exist \(L,\eta>0\), independent of \(h,N\), such that
\[
 N\int_{\Gamma_{h,y}} |K_N(z,y)|
 e^{N\{W_h(z)-\Re C(h)-W_{h^+}(y)\}}|dz|\le L
                                    \quad(y\in\Lambda).
 \tag{4}
\]
For local output also require the full complement of that arc,
including its connecting pieces, to satisfy
\[
 N\int_{\Gamma_{h,y}\setminus\gamma_{h,y}} |K_N(z,y)|
 e^{N\{W_h(z)-\Re C(h)-\Re S_{h^+}(y)\}}|dz|
          \le Le^{-\eta N}\qquad(y\in D_R).
 \tag{5}
\]
All domains may be chosen slightly larger than the final disk on
which derivatives are reported. These conditions concern the full
kernel and the full contour, including its joining pieces.

**Proposition.** Equation (4) implies the exact norm inequality
\[
          \|L_NG\|_{h^+,N}
                \le Le^{N\Re C(h)}\|G\|_{h,N}.
 \tag{6}
\]
Suppose in addition (2), (5), and an actual incoming packet
\[
 G_N(z)=c_NN^\nu e^{N(A+S_h(z))}f(z)(1+r_N(z))
       \quad(z\in D_R),\qquad
 \|r_N\|_\infty\le\epsilon_N,
 \tag{7}
\]
where \(c_N\ne0\), \(f=e^\ell\), \(\ell(0)=0\), and
\(\|\ell'\|\) belongs to the invariant amplitude class.
Assume the separate whole-message envelope
\[
          \|G_N\|_{h,N}\le Q|c_N|N^\nu e^{N\Re A}.
 \tag{8}
\]
Then the attached message has a packet of the same form, with
\[
 \begin{split}
 A^+&=A+C(h),\\
 c_N^+&=\kappa_N^3\mu(h,\ell)c_N,\\
 f^+(y)&=m_h(y)f(\chi_h(y))/\mu(h,\ell),\\
 m_h(y)&=\frac{\sqrt{2\pi}\,B(\chi_h(y),y)}
       {\sqrt{-S_h''(\chi_h(y))-\psi_{zz}(\chi_h(y),y)}},\\
 \mu(h,\ell)&=m_h(0)f(\chi_h(0))\ne0.
 \end{split}
 \tag{9}
\]
Its normalized error and envelope obey, with uniform constants,
\[
 \epsilon_N^+\le C\{\epsilon_N+N^{-1}+Qe^{-\eta N}\},
 \qquad Q^+\le LQ/|\mu(h,\ell)|.
 \tag{10}
\]
The phase map is unchanged. The basin's amplitude proof applies
with \(B\) in (9): it only uses a nonzero holomorphic kernel
coefficient and the contracting critical input. Its amplitude
bound may be chosen accordingly.

*Proof.* Substitute
\(|G(z)|\le\|G\|_{h,N}e^{NW_h(z)}\) into the exact
integral (1), deform to \(\Gamma_{h,y}\), and use (4).
This proves (6) directly. The exterior portion of the same
integral is bounded by (5) and (8). On its central portion,
(7) applies. The factor containing \(r_N\) is bounded using
(4); boundedness and nonvanishing of the normalized amplitudes
convert this to the first error term in (10).

The remaining central integral has the unique original saddle
\(\chi_h(y)\). Uniform local stationary phase using (2)
gives (9) and its \(O(N^{-1})\) error. The factors
\(N\), \(N^{-1/2}\) from (2), and \(N^{-1/2}\) from
this last Gaussian cancel, leaving \(N^\nu\). Local contour
ends lie away from the uniformly interior saddle and have a
strict phase gap. The original accretive root fixes the square
root and contour orientation. Equation (6), divided by the
new scalar in (9), gives the envelope bound in (10).
All estimates on slightly larger local disks give the same
fixed-order normalized derivative bounds by Cauchy's formula.
\(\square\)

Thus a fixed number of attachments propagates an actual entrance
with \(\epsilon_N=O(N^{-1})\), retains every action increment
and nonzero scalar, and prevents exterior cancellation of its
local leading packet. This does not assert contraction of the
finite-source error: \(L\) may exceed one. No simultaneous
limit with attachment number increasing with \(N\) follows.

## 3. A concrete sufficient exterior-rate test

There is a finite-dimensional possible route to (4)--(5). On
the prescribed contours the external exponentials \(X,Y\)
stay in compact subsets of \(0<|X|,|Y|<1\). The exact original
four-index row formula and uniform factorial bounds therefore give
\[
 |K_N(z,y)|\le C_0N^b e^{N B_{\rm phys}(z,y)},\qquad
 B_{\rm phys}(z,y)=\max_{\Omega}E(s,t,p,q;X,Y).
 \tag{11}
\]
This includes all three physical support inequalities and their
zero boundary rows, both cardinal factors, and all normal factors.
It does not require a far-wire saddle theorem.

The [exact outer-index elimination](research_mixed_contracted_pair_outer_index_elimination.md)
reduces the last maximum to
\[
 \max_{t,p\ge0,\ t+p\le1}
       \{C(t,p)+\max_s S_t(s)+\max_q Q_p(q)\}.
 \tag{12}
\]
Each outer maximum has the proved finite endpoint and stationary
candidate list. Only \(t,p\) and the external wire parameters
remain continuous; every candidate branch is retained.

On \(\gamma_{h,y}\), the completed coherent packet and the
chosen quadratic descent give the bounded central part of (4).
On all remaining contour pieces use a containing rate
\(\mathcal B(z,y)\): it may be \(\Re\psi(z,y)\) inside
the proved local kernel bidisk, and \(B_{\rm phys}(z,y)\)
elsewhere. On every noncentral piece, and on the whole input
contour when the output lies outside the local disk, the explicit
inequality
\[
 W_h(z)+\mathcal B(z,y)
       \le \Re C(h)+W_{h^+}(y)-\eta_0,
                 \qquad\eta_0>0,
 \tag{13}
\]
would give the remaining part of (4), and (5), after absorbing
the fixed polynomial in (11). In particular connecting pieces
are included in (13); they are not removed by the local Gaussian
calculation. The weights, contours and margins in (13) have
to be specified and proved; raw \(B_{\rm phys}\) is not
asserted to be sufficiently sharp. In particular its known
high-rate trials cannot be discarded or replaced by a coherent
rate outside the proved local kernel chart.

Finally the [actual cap-phase entrance](research_mixed_alternating_cap_phase_entrance.md)
constructs the original geometric phase and a nonzero local
current in the basin after a sufficiently long alternating tail.
It does not establish (7) for the whole finite message, (8) on
the whole period, or (13). The global transform in the exact
Fourier bridge still samples the entire physical circle. These
initial-source and exterior-operation estimates remain separate
from local phase entrance, and from the original final closing
functional required for a knot or cofinite-filling theorem.
