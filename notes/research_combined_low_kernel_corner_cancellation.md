# Cancellation of the actual low-kernel horizontal–vertical corners

Private written proof, 17 November 2026.

The nonzero upper-end asymptotic of an all-vertical current is not an
asymptotic of the corresponding combined current. For an arbitrary
fixed graph in the scope below, its adjoining original horizontal
pieces cancel that artificial endpoint. The cancellation is an exact
identity of finite source forms, before any asymptotic approximation.
The low-kernel formula then gives a fixed action loss for the joined
local chain. Coupled edge amplitudes and polynomial attachments remain.

This removes the specified excessive corner rate from the combined
local source. It does not bound the remaining contour by a geometric
action, or prove a lower bound for the original closing.

## 1. Exact original forms and the retained graph

Use the two complete direct sources [F] and [L] listed at the end.
Put \(D=N-1\), \(\eta=(-1)^D\),
\[
 C_{N,n}=\exp\{\pi i nD^2/(4N)\},\qquad
 \Omega_{N,n}=C_{N,n}e^{inN\pi/4},\qquad
 W_N(t)=\frac{e^{-iNt}}{(1-\eta e^{-iNt})^2}.
 \tag{1}
\]
Let \(K_N^{\rm low}\) be exactly [L](2), with its different middle
index at the two level parities. The high radical and its matching
terms have already been separated by that identity; none is deleted
or asserted to have the estimates below.

Let \(G=(V,E)\) be a fixed nonempty finite loopless simple graph, all
of whose vertices are selected and have \(d_v=\deg v\ge1\).
Write \(a=|V|\) and \(b=|E|\).
Assign integers \(n_v\ne0\) and fixed heights \(H_v>0\), and assume
\[
              \lambda_v=\frac{d_v+|n_v|}{2}-1>0.
 \tag{2}
\]
This is precisely the endpoint-maximizing degree/power condition of
[L], not a claimed property of every partial filling.
For the quantitative bare-graph result the attachment is \(A_N=1\).
The exact identities also allow any joint polynomial
\(A_N((C_v)_{v\in V};\zeta)\), with any other variables or original
exterior coefficients denoted by \(\zeta\). It need not factor by vertex.

The original full Hermite functional is
\(\phi_N(f)=\eta N^2[C^D]\operatorname{rem}_{P_N}f\), with
\(P_N(C)=2T_N(C/2)+2\).
For unit charge, [F](7) gives the exact operator identity
\[
 \phi_N(R^{n_v}f)=H_v^{\rm op}[f]+V_v^{\rm op}[f],
 \quad
 H_v^{\rm op}[f]=-\frac{N^2C_{N,n_v}}{\pi i}
  \int_{-\pi-iH_v}^{\pi-iH_v}
   \sin t\,W_N(t)e^{in_vNt^2/(4\pi)}f(-2\cos t)\,dt.
 \tag{3}
\]
Here \(V_v^{\rm op}[f]=\int_0^{H_v}\rho_{N,n_v,1}(h)f(2\cosh h)\,dh\)
is the full paired vertical current of [F](11). Formula (3) retains
the original value and first normal at every double physical root
and the odd simple-node value.

The Gaussian in (3) is the specified off-grid representative in this
exact trace formula. It is not asserted equal to the canonical
polynomial \(R^{n_v}(C)\) at free complex \(C\). Every deformation below
uses this same exact Gaussian form on both pieces; no comparison of
two off-grid representatives is needed.

For \(\sigma=\pm1\) use the chart
\[
 t=\sigma\pi-ih,\qquad C=2\cosh h,
\]
and define the exact one-form
\[
 \omega_{v,\sigma}(h)=
 -\frac{i\eta N^2\Omega_{N,n_v}}{\pi}
 \frac{\sinh h}{(1+e^{-Nh})^2}
 \exp N\left[\left(\frac{\sigma n_v}{2}-1\right)h
                         -\frac{i n_vh^2}{4\pi}\right]dh .
 \tag{4}
\]
Indeed \(\sin t=i\sinh h\), \(dt=-i\,dh\), and
\(W_N(t)=-\eta e^{-Nh}/(1+e^{-Nh})^2\). Substitution into (3)
gives (4), with its sign. Directly from the paired density,
\[
                  \rho_{N,n_v,1}(h)\,dh
                          =-\omega_{v,+}(h)+\omega_{v,-}(h).
 \tag{5}
\]
These identities hold at every level.

## 2. The exact local chain identity, including all intersections

Put \(\sigma_v=\operatorname{sgn}n_v\). Choose a small fixed
\(0<\delta_v<H_v/2\), and abbreviate
\[
 a_v=H_v-i\sigma_v\delta_v,\qquad b_v=H_v-\delta_v.
 \tag{6}
\]
The dominant horizontal endpoint piece in (3) is
\(\pi-\delta_v-iH_v\to\pi-iH_v\) for \(n_v>0\), and
\(-\pi-iH_v\to-\pi+\delta_v-iH_v\) for \(n_v<0\).
In the \(h\)-chart its oriented integral is
\(\sigma_v\int_{a_v}^{H_v}\omega_{v,\sigma_v}\).
Keep the *entire paired* vertical segment \(b_v\to H_v\).
Equations (4),(5) therefore give the exact local replacement
\[
 \boxed{\quad
 \mathfrak H_v+\mathfrak V_v
   =\sigma_v\int_{a_v}^{b_v}\omega_{v,\sigma_v}
       +\sigma_v\int_{b_v}^{H_v}\omega_{v,-\sigma_v}.
 \quad}
 \tag{7}
\]
Each integral here acts coefficientwise on the unchanged attachment
and kernels. The first path on the right may be the straight segment.
The equality follows by Cauchy's theorem in the triangle with vertices
\(a_v,H_v,b_v\). It is contained in \(\Re h>0\), so
\((1+e^{-Nh})^{-2}\) has no pole there. All low kernels and polynomial
attachments are holomorphic there.

The second term in (7) is essential: the paired current has not been
replaced by just its dominant Gaussian branch. In fact
\[
                  \omega_{v,-\sigma_v}
                       =e^{-N|n_v|h}\omega_{v,\sigma_v}.
 \tag{8}
\]

Tensor (7) over any subset \(C\subseteq V\), with every other variable,
trace or contour kept as a coefficient. This gives an exact identity
for all \(2^{|C|}\) local horizontal/paired-vertical terms, with the
same shared kernel factors in each term. Finite Fubini and Cauchy's
theorem apply without factorizing those kernels. Consequently this
identity includes corners of every codimension and their intersections.
It is also compatible with the full-survivor inclusion–exclusion
formula [F](16): expand it back to \(\prod(H_v^{\rm op}+V_v^{\rm op})\)
before grouping these local pieces.

For the full upper corner define
\[
 \mathcal J_N^{\rm corner}[A_N]
  =\left(\prod_{v\in V}(\mathfrak H_v+\mathfrak V_v)\right)
        \left[A_N(\mathbf C;\zeta)
                     \prod_{vw\in E}K_N^{\rm low}(C_v,C_w)\right].
 \tag{9}
\]
This is a specified sum of pieces of the actual original trace,
not a new invariant or an independently normalized current.

## 3. A fixed loss for that actual combined corner

Choose the \(\delta_v\) small enough that the product of the triangles
in Section 2 lies in the complex positive-height neighborhood of
[L], Lemma 1. That lemma gives, with fixed derivatives,
\[
 K_N^{\rm low}(2\cosh h_v,2\cosh h_w)
  =N^{-2}e^{N(h_v+h_w)/2}
       \{\mathcal K_{\epsilon}(h_v,h_w)+O_{\rm hol}(N^{-2})\}.
 \tag{10}
\]
Its coupled coefficient is bounded on a fixed larger neighborhood.
The exact expression obtained by dividing the left side by its
displayed exponential has the same uniform bounds. We use that
exact expression, not only its leading symbol.

Let
\[
 \Phi_v(h)=\lambda_vh-\frac{i n_vh^2}{4\pi},\qquad
 R=\sum_v\lambda_vH_v,\qquad
 M_N=\sup_{\mathcal U}|A_N((2\cosh h_v)_v;\zeta)| ,
 \tag{11}
\]
where \(\mathcal U\) is this fixed larger product neighborhood and a
fixed exterior-parameter compact. For \(A_N=1\), \(M_N=1\).
Any dependence of \(M_N\) on \(N\), including an exponential cost,
is retained.

Factoring (10) from the product of the dominant forms (4) leaves
\[
 \left(-\frac{i\eta}{\pi}\right)^a
       \left(\prod_v\Omega_{N,n_v}\right)N^{2a-2b}
       \mathcal A_N(\mathbf h;\zeta)
                     e^{N\sum_v\Phi_v(h_v)}\prod_vdh_v,
 \tag{12}
\]
where \(|\mathcal A_N|\le C M_N\). All fixed derivatives have the
corresponding bounds by Cauchy on a smaller buffered neighborhood.
The exact finite denominator in (4) remains in \(\mathcal A_N\).

On the straight connector in (7), write
\(h=H_v-s-i\sigma_v t\), where \(s,t\ge0\) and
\(s+t=\delta_v\). There is the exact quadratic identity
\[
 \Re\Phi_v(h)-\Re\Phi_v(H_v)
       =-\lambda_vs-\frac{|n_v|}{2\pi}t(H_v-s)
       \le-\delta_v\mu_v,\qquad
 \mu_v=\min\left\{\lambda_v,\frac{|n_v|H_v}{4\pi}\right\}>0 .
 \tag{13}
\]
On the opposite-branch vertical in (7), \(b_v\le h\le H_v\);
the dominant real action is at most \(\lambda_vH_v\), while (8)
supplies a loss at least \(|n_v|(H_v-\delta_v)\). Set
\[
 \Delta=\sum_{v\in V}
      \min\{\delta_v\mu_v,\ |n_v|(H_v-\delta_v)\}>0.
 \tag{14}
\]
Every one of the \(2^a\) terms on the right of the tensorized (7)
therefore has action at most \(R-\Delta\).
All path lengths are bounded independently of \(N\). Thus:
\[
 \boxed{\qquad
 |\mathcal J_N^{\rm corner}[A_N]|
       \le C M_N N^{2a-2b}e^{N(R-\Delta)} .
 \qquad}
 \tag{15}
\]
The constants depend on the fixed graph, powers, heights and chosen
buffers, not on the level. Both parities are included.
For bounded holomorphic exterior parameter families, fixed derivatives
obey (15) with the appropriate buffered attachment norm and at most
additional fixed powers of \(N\). Original finite value/normal
functionals may instead be applied exactly after (7); their dual cost
is not silently included in \(C\).

This directly compares with [L]'s all-vertical result
\(\mathcal I_N^{\rm low}\sim \mathcal B_N N^{a-2b}e^{N\sum_v\Phi_v(H_v)}\),
whose coefficient is nonzero for the bare graph. The global bound
[L](23) gives a loss at least \(\min_v\lambda_v\delta_v>0\)
outside the top vertical box, so its rate-\(R\) coefficient belongs
to the corner included in (9).
Equation (15) proves that this coefficient is canceled by the original
companion horizontal pieces. The cancellation does not require a
special attachment value, positivity of an attachment, or a new
choice of crossing scalar.

For a lower-dimensional corner \(C\), the exact statement (7) is
unconditional. A quantitative version of (15) follows using the
induced graph \(G[C]\), degrees \(d_C(v)\), and
\(\lambda_{v,C}=(d_C(v)+|n_v|)/2-1>0\), while all cut edges and
surviving factors are retained in \(A_N\). Their actual local norm
must then appear in \(M_N\). Neither the full-degree condition (2)
nor a global geometric parent is asserted to imply these induced
inequalities or a tame exterior norm at every face.

## 4. Cancellation of every artificial endpoint jet

The preceding proof uses exact holomorphy and a fixed gap, rather than
truncating an endpoint expansion. There is also a direct jet check.
On the neighborhoods in use, \(\Phi_v'\ne0\). For an exact holomorphic
amplitude \(B\), define
\[
 B_0=B,\qquad B_{r+1}=\partial_{h_v}(B_r/\Phi_v').
 \tag{16}
\]
Repeated integration by parts in that coordinate gives the exact
endpoint terms
\[
 \sum_{r=0}^{L-1}(-1)^rN^{-r-1}
       \left[\frac{B_r}{\Phi_v'}e^{N\Phi_v}\right]_{\rm start}^{\rm end}
 \tag{17}
\]
plus its retained integral remainder. In the dominant pair on the
left of (7), the endpoint \(h_v=H_v\) occurs once with coefficient
\(\sigma_v\) and once with coefficient \(-\sigma_v\).
Its exact terms (17) cancel for every \(r\), before any approximation
of \(B\). In (12), \(B\) contains all derivatives of the actual
coupled kernels and attachment; these have not been frozen at the
corner. Operators (16) in distinct coordinates commute because the
phase is separated, so the same cancellation holds at every mixed
endpoint jet and every intersection of faces.

The opposite branch (8) is retained rather than canceled by this
argument. Its strict loss was paid explicitly in (14).

## 5. Coverage and remaining scope

The local removal of an artificial holomorphic corner is an established
method; the archived incoming half-face proof applies it to a different
fixed packet. The additional assertion here is its exact application
to the arbitrary-graph low-kernel obstruction, with the original
Gaussian trace carrier, both vertical branches, all shared edge
amplitudes, the explicit loss (13)--(15), and endpoint jets retained.
The proof above supplies its own chain and phase calculation.

No canonical-polynomial substitution has been made on a free complex
color. The full source is preserved through (3) and (7), and any
original covector remains the same linear observation throughout.
Protected zeros or other coefficient selections in an exterior are
not relaxed by treating that exterior coefficientwise.

Only fixed neighborhoods of the artificial upper corners are removed.
The new connector endpoints, the remaining horizontal and vertical
pieces, all high-radical matching terms, and any other source cut or
alias still remain. The positive number \(\Delta\) is measured from
the excessive corner rate \(R\); no comparison with the selected
geometric action is proved. In particular (15) supplies neither an
arbitrary-short-filling theorem nor a nonzero final observation.

Both complete direct texts were read in full and their used
implications checked at these pins:

* [F: Full-period original trace and current](research_full_period_current_charge_convolution.md),
  SHA256 3f74b9824ecbf0b71a79b17959c7208f650103f95932192cfba87c7a7aa05595.
* [L: Actual remaining low-kernel asymptotic](research_low_kernel_all_removed_current_asymptotic.md),
  SHA256 e9261e460fe52989ea298f423acc699a4e4b34c00805efbe52c5bee8eb2c1161.

The full archived local-corner proof was also read for coverage; none
of its packet-specific hypotheses is imported. Only written mathematics,
source reads and metadata hashes were used. No mathematical program,
numerical experiment, test or build was run. Frozen sources and public
manuscripts are unchanged.
