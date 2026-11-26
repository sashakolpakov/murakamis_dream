# A filled crossing as an exact polynomial trace

The operator obtained by filling one crossing circle is an actual fixed power of the crossing. It can therefore be studied without first expanding that power in the moving auxiliary-color basis. The result below is local: it applies to a fixed product of regular low Newton factors at one crossing-circle junction. It supplies a nonzero leading term, an exponentially accurate analytic interpolation in the incident wire variables, and its exact dependence on the microscopic main meridian. Section 6 identifies its action with the marked long-filling action. The last section explains how the local estimate enters the [grouped wire packet](actual_main_meridian_grouped_wire_packet.md) and why the [joint filling transform](actual_main_meridian_joint_filling_transform.md) is needed when different twist powers are independently long.

The polynomial coordinates and the typed crossing are fixed by the [Newton compiler](actual_main_meridian_newton_compiler.md) and the [turn comparison](actual_main_meridian_turn_comparison.md). The canonical sine-factorial interpolation used below is also derived in the [regular circle trace](actual_main_meridian_regular_circle_trace.md), Section 10. All crossing powers are fixed before the level tends to infinity.

## 1. The finite operator and the statement

Put
\[
 q=e^{\pi i/N},\quad d=N-1,\quad \eta=(-1)^{N-1},\qquad
 P_s(z)=T_N(z)+2\cos(2\pi s),
 \tag{1}
\]
where \(T_N(2\cos t)=2\cos Nt\) is monic. The fixed complete Newton basis is
\[
 e_k(z)=\frac{\prod_{a=0}^{k-1}(c_a-z)}{S_k^2},\qquad
 c_a=2\cos\frac{(2a+1)\pi}{N},\quad
 S_k=\prod_{a=1}^k2\sin\frac{\pi a}{N}.
 \tag{2}
\]
We use the original Frobenius functional
\[
 \phi_s(f)=\eta N^2[z^{N-1}](f\bmod P_s).
 \tag{3}
\]
The crossing \(R_s\) includes its physical Cartan scalar. At a generic root, write
\[
 \tau_r(s)=\frac{2\pi}{N}\left(\frac d2+s-r\right),\quad
 z_r(s)=-2\cos\tau_r(s),\quad 0\le r<N.
 \tag{4}
\]
Its exact full eigenvalue is
\[
 R_s(z_r(s))
 =q^{d^2/4-s^2/2}
       \exp\left(\frac{iN\tau_r(s)^2}{4\pi}\right).
 \tag{5}
\]
In particular, for any fixed integer \(n\),
\[
 C_{N,n}(s)=q^{n(d^2/4-s^2/2)},\qquad
 R_s^n(z_r(s))=
 C_{N,n}(s)\exp\left(\frac{inN\tau_r(s)^2}{4\pi}\right).
 \tag{6}
\]
All root collisions in \(|s|<1\) are interpreted by the actual holomorphic crossing polynomial and its full normal coefficients. The [Newton compiler](actual_main_meridian_newton_compiler.md) and [physical crossing bounds](actual_main_meridian_source_bounds.md), Section 1.3, make \(R_s\), its inverse, and every fixed power holomorphic on this disk. The first nonremovable same-color interpolation resonance is at \(s=\pm1\), outside the present statement.

Fix an integer \(B\ge1\), a compact interval
\(I=[\delta,1/2-\delta]\subset(0,1/2)\), and \(0\le R<1\). For integer indices \(k_a/N\in I\), let
\[
 E_{N,\mathbf k}(z)=\prod_{a=1}^B e_{k_a}(z),\qquad
 V_{N,s}^{(n)}(\mathbf k)=\phi_s(R_s^nE_{N,\mathbf k}).
 \tag{7}
\]
There is \(n_0=n_0(I,B)\) such that, for each fixed integer \(|n|\ge n_0\), the complete tensor \(V_{N,0}^{(n)}(\mathbf k)\) is nonzero for all sufficiently large \(N\), uniformly over these indices. Moreover, there is \(\kappa>0\), depending on the fixed data including \(n\) and \(R\), for which
\[
 \boxed{\displaystyle
 \frac{V_{N,s}^{(n)}(\mathbf k)}
      {V_{N,0}^{(n)}(\mathbf k)}
 =q^{-ns^2/2}\bigl(1+O(e^{-\kappa N})\bigr),
 \qquad |s|\le R<1.}
 \tag{8}
\]
Both parities are included. The integer \(n\) is fixed before \(N\) tends to infinity. The statement does not concern a growing filling coefficient \(n=n(N)\).

The proof gives an analytic interpolation in the complex variables \(x_a=k_a/N\). Its main-meridian ratio is exactly \(q^{-ns^2/2}\). Thus (8) is more than a comparison on a real lattice, but it is still a local junction result.

## 2. An exact contour with the actual crossing power

For this section set
\[
 B_N(\tau)=\sin\tau\,E_{N,\mathbf k}(-2\cos\tau)
                   e^{inN\tau^2/(4\pi)}.
 \tag{9}
\]
This is an entire odd function. Lagrange interpolation at the generic roots gives
\[
 V_{N,s}^{(n)}
 =\frac{\eta N C_{N,n}(s)}{\sin(2\pi s)}
          \sum_{r=0}^{N-1}B_N(\tau_r(s)).
 \tag{10}
\]
Indeed \(P_s'(z_r)=N\sin(2\pi s)/\sin\tau_r\), and (3) gives the remaining \(\eta N\). The formula initially excludes the zeros of its displayed sine; analytic continuation later restores the full normal trace.

Choose \(R'\) with \(R<R'<1\) and \(R'\ne1/2\). We first estimate (10) only on the parameter circle \(|s|=R'\). On this circle \(|\sin(2\pi s)|\) is bounded below by a positive constant. Put
\[
 \Delta_s=\frac{2\pi s}{N},\qquad
 K_s(\tau)=\frac{iN e^{iN\tau}}
                    {e^{iN\tau}-\eta e^{2\pi is}}.
 \tag{11}
\]
Let \(\mathcal R_y+\Delta_s\) be the positively oriented rectangle with vertices \(\pm\pi\pm iy+\Delta_s\). It contains exactly the \(N\) points (4), for fixed \(y>0\) and sufficiently large \(N\). Each pole of \(K_s\) has residue one, so
\[
 \sum_r B_N(\tau_r(s))
 =\frac1{2\pi i}\int_{\partial(\mathcal R_y+\Delta_s)}
                      B_N(\tau)K_s(\tau)\,d\tau.
 \tag{12}
\]
The translation matters when \(|\operatorname{Re}s|\ge1/2\). It keeps the vertical sides halfway between their neighboring grid poles. At
\(\tau=\pm\pi+iv+\Delta_s\), one has exactly
\[
 e^{iN\tau}=-\eta e^{2\pi is}e^{-Nv},
 \qquad
 K_s(\tau)=\frac{iN e^{-Nv}}{1+e^{-Nv}}.
 \tag{13}
\]
There is consequently no vertical pole-separation assumption on the argument of \(s\).

On the upper horizontal side the convergent geometric expansion is
\[
 K_s(\tau)=-iN\sum_{\ell\ge1}
          \eta^\ell e^{-2\pi i\ell s}e^{i\ell N\tau},
 \tag{14}
\]
and on the lower side it is
\[
 K_s(\tau)=iN\left(1+\sum_{\ell\ge1}
          \eta^\ell e^{2\pi i\ell s}e^{-i\ell N\tau}\right).
 \tag{15}
\]
The terms are entire functions of \(\tau\). Their horizontal integration paths can therefore be moved to the fixed sides \([-\pi,\pi]\pm iy\); the short endpoint connectors stay within \(O_R(1/N)\) of the old vertical sides. No deformation of the meromorphic kernel through a moving pole is being asserted here.

Define the fixed lower-side integrals
\[
 I_{\ell,N}^{(n)}(y)
 =\int_{-\pi-iy}^{\pi-iy}
   \sin\tau\,E_{N,\mathbf k}(-2\cos\tau)
       e^{inN\tau^2/(4\pi)-i\ell N\tau}\,d\tau.
 \tag{16}
\]
The upper side, with its boundary orientation, contributes the same \(I_\ell\) after \(\tau\mapsto-\tau\), because \(B_N\) is odd. The difference of the two coefficients in (14)--(15) is \(2i\sin(2\pi\ell s)\). The zero mode in (15) has zero integral on the real segment by oddness; moving its lower path to that segment produces only endpoint currents. Thus
\[
 V_{N,s}^{(n)}
 =-\frac{N^2C_{N,n}(s)}{\pi i}
    \sum_{\ell\ge1}
       \eta^{\ell-1}
       U_{\ell-1}(\cos2\pi s)\,I_{\ell,N}^{(n)}(y)
       +\mathcal E_{N,s}(y).
 \tag{17}
\]
Here \(U_{\ell-1}(\cos z)=\sin(\ell z)/\sin z\), and
\(\mathcal E_{N,s}\) contains the original two vertical sides, the endpoint connectors, and the zero-mode endpoint currents. Formula (17) is first justified on \(|s|=R'\), where (10) has a bounded denominator. It is an exact convergent contour decomposition there, not a Poisson expansion of a nonperiodic real chirp.

For clarity, the sign and normalization in (17) can also be checked on \(|s|<1/2\) with the paired kernel
\[
 \frac{e^{iN\tau}}
 {(e^{iN\tau}-\eta e^{2\pi is})
  (e^{iN\tau}-\eta e^{-2\pi is})}.
 \tag{18}
\]
Its two horizontal expansions have coefficients
\(\eta^{\ell-1}U_{\ell-1}(\cos2\pi s)\), and its prefactor is
\(-N^2C_{N,n}/(2\pi i)\). The two sides give the factor two in (17). This check does not impose the smaller radius on the translated-contour proof.

## 3. The finite Newton action and the first saddle

Normalize the Newton product at its positive maximum:
\[
 A_N(\tau)=\frac1N
    \log\frac{E_{N,\mathbf k}(-2\cos\tau)}
                   {E_{N,\mathbf k}(-2)}.
 \tag{19}
\]
There is a fixed neighborhood of zero on which the logarithm is analytic, even, and real on the real axis, uniformly for all allowed indices. The product formula (2) gives
\[
 A_N(0)=0,\qquad
 A_N''(0)=-a_N,\qquad
 a_N=\frac1{2N}\sum_{a=1}^B\sum_{r=0}^{k_a-1}
                 \sec^2\frac{(r+1/2)\pi}{N}.
 \tag{20}
\]
In particular, \(a_-\le a_N\le a_+\) for fixed positive constants. Midpoint integration gives
\[
 a_N=\frac1{2\pi}\sum_{a=1}^B\tan(\pi x_a)+O(N^{-2}),
 \qquad x_a=k_a/N.
 \tag{21}
\]
All derivatives of \(A_N\) on a smaller fixed complex disk are uniformly bounded. Its local expansion is
\[
 A_N(\tau)=-\frac{a_N\tau^2}{2}+O(\tau^4).
 \tag{22}
\]
We also use the established global Newton strip bound: for each fixed small real \(\rho>0\), there are \(c_\rho,y_\rho>0\) such that
\[
 |E_{N,\mathbf k}(-2\cos(t+iv))|
 \le N^C E_{N,\mathbf k}(-2)
             e^{-c_\rho N+C Nv^2},
 \quad \rho\le|t|\le\pi+O_R(N^{-1}),\
       |v|\le y_\rho+O_R(N^{-1}).
 \tag{23}
\]
It follows directly from the positive low-Newton Laurent profile and its strict angular maximum. Its use here is for the raw product, not for a high-degree canonical reduction.

For the first Fourier term put
\[
 \Phi_{1,N}(\tau)
 =A_N(\tau)+\frac{in\tau^2}{4\pi}-i\tau.
 \tag{24}
\]
Its critical equation can be written
\[
 \tau=\frac{2\pi}{n}
             +\frac{2\pi i}{n}A_N'(\tau).
 \tag{25}
\]
The analytic implicit function theorem at \(1/n=0,\tau=0\), with the uniform bounds above, gives a unique critical point in the chosen neighborhood for \(|n|\) sufficiently large. Uniformly in the index window,
\[
 \tau_{*,N}
 =\frac{2\pi}{n}
       -\frac{4\pi^2ia_N}{n^2}+O(|n|^{-3}),
 \tag{26}
\]
\[
 \Phi_{1,N}(\tau_{*,N})
 =-\frac{i\pi}{n}
       -\frac{2\pi^2a_N}{n^2}+O(|n|^{-3}).
 \tag{27}
\]
These formulas are valid for both signs of \(n\). In particular
\(\operatorname{Im}\tau_{*,N}<0\), and
\(\sin\tau_{*,N}\ne0\).

Move (16), for \(\ell=1\), to the horizontal line through this critical point. The endpoint currents satisfy (23). On a fixed small interval around \(\operatorname{Re}\tau_*\), the real part of the second derivative remains negative, and outside that interval the local quadratic bound or (23) gives a strict loss. The ordinary analytic Gaussian expansion therefore gives
\[
 I_{1,N}^{(n)}
 =E_{N,\mathbf k}(-2)e^{N\Phi_{1,N}(\tau_{*,N})}
      \sin\tau_{*,N}
      \sqrt{\frac{2\pi}{-N\Phi_{1,N}''(\tau_{*,N})}}
       \bigl(1+O_n(N^{-1})\bigr).
 \tag{28}
\]
The square root has the branch determined by the oriented horizontal contour; equivalently its denominator has positive real part at zero chirp and is continued along the actual quadratic phase. This leading coefficient is nonzero. The constants may depend on the fixed \(n\), but are uniform over the wire window.

## 4. One height controls every higher Fourier term

Choose a smaller fixed local radius so that
\[
 \operatorname{Re}A_N(t-iy)
       \le-\frac{3a_N}{8}t^2+C y^2
 \tag{29}
\]
there. This follows from (22), the positive lower bound for \(a_N\), and the fact that the first change in the real part under an imaginary displacement is quadratic in \(y\). Set
\[
 y=\frac{8\pi^2a_N}{n^2}.
 \tag{30}
\]
For large fixed \(|n|\), this height lies in the local strip. On its lower side the real exponent of the \(\ell\)-th term is bounded by
\[
 -\frac{3a_N}{8}t^2
       +\frac{|n|\,|t|y}{2\pi}
       -\ell y+C y^2.
 \tag{31}
\]
Maximizing the first two terms over \(t\) gives
\[
 \frac{n^2y^2}{6\pi^2a_N}.
 \tag{32}
\]
For \(\ell=2\), substitution of (30) into (31)--(32) gives
\[
 -\frac{16\pi^2a_N}{3n^2}+O(n^{-4}).
 \tag{33}
\]
By increasing \(n_0\), this is at most
\(-\tfrac92\pi^2a_N/n^2\), whereas (27) has real part at least
\(-\tfrac52\pi^2a_N/n^2\). Every \(\ell>2\) has the additional loss
\(-(\ell-2)y\).

On the complementary angular interval, the chirp has modulus at most
\(\exp(N|n||t|y/(2\pi))\), whose exponent is \(O(N/|n|)\). Thus (23) still gives a fixed strict angular loss for all sufficiently large \(|n|\). The same argument controls the vertical sides and the endpoint connectors in Section 2. Their imaginary heights are at most \(y+O_R(N^{-1})\); the chirp cost is \(O(N/|n|)\), while their Newton loss is a fixed multiple of \(N\). The factors \(K_s\) on the translated vertical sides are only \(O(N)\) by (13).

The infinite sum is also controlled. On the parameter circle,
\[
 |U_{\ell-1}(\cos2\pi s)|
 \le \ell e^{2\pi R'(\ell-1)}.
 \tag{34}
\]
The additional \(\exp(-N(\ell-2)y)\) makes the sum of all \(\ell\ge2\) a convergent geometric tail for large \(N\). The connector estimates can be summed in the same way, since their heights differ from \(y\) by only \(O_R(N^{-1})\). We have proved, uniformly on \(|s|=R'\),
\[
 V_{N,s}^{(n)}
 =-\frac{N^2 C_{N,n}(s)}{\pi i}\,I_{1,N}^{(n)}
  +O\!\left(
       |I_{1,N}^{(n)}|\,N^2 e^{-\kappa N}\right)
 \tag{35}
\]
for some positive \(\kappa\), after shrinking it to absorb polynomial factors.

Now define the *whole* difference between the left side of (35) and its displayed first-term approximation. Both are holomorphic for \(|s|<1\), including \(s=0,\pm1/2\). The maximum principle transfers the boundary estimate to \(|s|\le R\). This argument does not claim that the separately divided endpoint errors in (10) are individually removable. Evaluating (35) at \(s=0\), using (28), and dividing proves (8).

Uniform holomorphy on a slightly larger disk gives the corresponding estimates for every fixed \(s\)-derivative on the smaller disk.

## 5. A specified analytic wire interpolation

The preceding proof controls actual integer indices. To move wire contours, use the canonical sine-factorial function
\[
 G_N(z)=\left(\frac{2\pi}{N}\right)^z\Gamma(z+1)
 \prod_{m\ge1}
 \frac{\Gamma(Nm+z+1)}
      {\Gamma(Nm-z)(Nm)^{2z+1}}.
 \tag{36}
\]
On \(-1<\operatorname{Re}z<N\), it is holomorphic and nonzero, with the fixed positive-base logarithms, \(G_N(k)=S_k\), and
\[
 \frac{G_N(z+1)}{G_N(z)}
       =2\sin\frac{\pi(z+1)}{N}.
 \tag{37}
\]
Its uniform complex bulk expansion is established in [exact factorial interpolation](exact_factorial_interpolation_and_complex_contours.md) and is used below. Put \(u=N\tau/(2\pi)\) and
\[
 \mathcal E_N(x,\tau)=
 \frac{G_N(d/2+u)G_N(d/2-u)}
 {G_N(d/2-Nx+u)G_N(d/2-Nx-u)G_N(Nx)^2}.
 \tag{38}
\]
For every physical \(x=k/N\), the shift equation (37) gives exactly
\(\mathcal E_N(k/N,\tau)=e_k(-2\cos\tau)\). For \(x\) in a fixed small complex neighborhood of \(I\) and \(\tau\) in a sufficiently small fixed disk, all arguments of (38) stay in regular bulk strips.

Choose a fixed small \(a>0\) containing all the first saddles for \(|n|\ge n_0\), and define
\[
 \mathfrak V_{N,s}^{(n)}(\mathbf x)
 =-\frac{N^2C_{N,n}(s)}{\pi i}
     \int_{-a}^{a}\sin\tau\,
       \prod_{j=1}^B\mathcal E_N(x_j,\tau)
       e^{inN\tau^2/(4\pi)-iN\tau}\,d\tau.
 \tag{39}
\]
This is jointly holomorphic in the complex wire variables and in \(s\). After shrinking the wire neighborhood, the saddle stays inside the contour endpoints and its amplitude remains nonzero. The argument of Sections 3--4, with the omitted angular tails included among the endpoint errors, gives on every physical grid point
\[
 V_{N,s}^{(n)}(\mathbf k)
 =\mathfrak V_{N,s}^{(n)}(\mathbf k/N)
             \bigl(1+O(e^{-\kappa N})\bigr).
 \tag{40}
\]
The comparison is exponential before any subsequent wire cancellation. The interpolant itself has the exact ratio
\[
 \boxed{\displaystyle
 \frac{\mathfrak V_{N,s}^{(n)}(\mathbf x)}
      {\mathfrak V_{N,0}^{(n)}(\mathbf x)}
      =q^{-ns^2/2}.}
 \tag{41}
\]
Thus there is no unspecified meridian-dependent local amplitude.

For later action comparison, the limiting Newton action is
\[
 b(x,\tau)=
 \int_0^x
 \log\frac{\cos(\pi v+\tau/2)\cos(\pi v-\tau/2)}
              {\sin^2(\pi v)}\,dv,
 \tag{42}
\]
with the real branch at \(\tau=0\) continued inside the fixed disk. Its second derivative there is
\(-\tan(\pi x)/(2\pi)\). For the junction, write
\(b(\mathbf x,\tau)=\sum_jb(x_j,\tau)\). The action selected by (39) is exactly
\[
 \mathcal T_n(\mathbf x)
 =\operatorname{stat}_{\tau}
       \left[b(\mathbf x,\tau)
                    +\frac{in\tau^2}{4\pi}-i\tau\right],
 \tag{43}
\]
on the branch near \(\tau=2\pi/n\). The unit factor
\(q^{nd^2/4}\) in (39) remains outside this action; it is not silently reset.

## 6. Equality with the original marked filling action

Let the original local crossing sign be \(\epsilon\in\{0,\pm1\}\), and let \(p\) be its integer auxiliary filling coefficient, so that the literal remaining crossing is \(R^n\), with
\[
 n=\epsilon-2p.
 \tag{44}
\]
The [regular circle trace](actual_main_meridian_regular_circle_trace.md), Sections 6–7, identifies the selected local action of the colored source packet as
\[
 f_\epsilon(\mathbf x,t)
 =\operatorname{stat}_{\tau}
       \left[b(\mathbf x,\tau)
              +\frac{i\epsilon\tau^2}{4\pi}+it\tau\right].
 \tag{45}
\]
This identity uses the actual auxiliary deficit and the old shear branch, not a new polarization convention. In the auxiliary Fourier transform, add \(2\pi i t z\). Stationarity in \(t\) imposes \(\tau=-2\pi z\). Since \(b\) is even in \(\tau\), the resulting action is
\[
 \Psi(\mathbf x,z)=b(\mathbf x,2\pi z)+i\pi\epsilon z^2.
 \tag{46}
\]
The original filling functional subtracts \(2\pi i(pz^2+z)\). Substitution of (44) and \(\tau=2\pi z\) gives
\[
 \Psi(\mathbf x,z)-2\pi i(pz^2+z)
 =b(\mathbf x,\tau)+\frac{in\tau^2}{4\pi}-i\tau.
 \tag{47}
\]
This is precisely the direct first-Fourier-term action in (43), including its charge, its sign, and the primitive filling coefficient.

The other wire variables can be included before taking stationarity in (45)--(47). Hence the selected joint critical point of the direct model is the old selected long-filling critical point, on its original marked branch. Under the hypotheses of the [strict-tree filling theorem](actual_conway_all_strict_tree_long_twist_volume.md) and its [marked geometry](actual_conway_general_mask_marked_filling.md), the geometric calibration identifies the real part of the resulting *whole* critical action with
\(\operatorname{Vol}(S^3\setminus K)/(2\pi)\), where only the auxiliary circles are filled and the knot cusp remains complete. This action identity does not require any new moving auxiliary-filling coefficient formula.

The topological normalization is also unchanged: the actual filled local operator is \(R_s^{\epsilon-2p}\), not an asymptotic replacement. The physical Cartan factors \(C_{N,n}(s)\), all six typed edge factors, and the original ribbon/closing scalar \(\zeta_N(s)\) must still be multiplied exactly. In particular, a final profile must retain
\(\zeta_N(s)/\zeta_N(0)\). No claim that this ratio tends to one is needed for logarithmic volume equality.

## 7. Global majorants and the whole-source interface

There is a useful global local majorant. For all low incident indices, including their endpoints, (10), evaluated on \(|s|=R'\ne1/2\), gives
\[
 |V_{N,s}^{(n)}(\mathbf k)|
       \le C_{n,R',B}N^2 E_{N,\mathbf k}(-2).
 \tag{48}
\]
Indeed the shifted root heights are \(O(1/N)\), the full fixed-power chirp is bounded on them, and the positive Laurent coefficients bound the raw product by a constant times its value at \(-2\). At completeness,
\[
 \phi_0(L_NE_{N,\mathbf k})
       \ge N(\pi/4)^B E_{N,\mathbf k}(-2)
 \tag{49}
\]
at both parities, with the sharper odd constant one. The actual trace is holomorphic on \(|s|<1\), so the maximum principle proves the all-low comparison
\[
 |V_{N,s}^{(n)}(\mathbf k)|
 \le C_{n,R,B}N\,\phi_0(L_NE_{N,\mathbf k}),
 \qquad |s|\le R<1.
 \tag{50}
\]
This comparison is with the old complete positive circle tensor, not with a filled signed tensor.

For a fixed tree in the [source-bound class](actual_main_meridian_source_bounds.md), or its [component extension](actual_main_meridian_component_extension.md), the grouped high-error induction uses a polynomial spectral bound for a fixed crossing power at a decorated junction. That bound is available for \(R_s^n\). Together with (50), the original strict positive action therefore controls high labels and the complement of the selected low window at a rate \(F_0-\eta\). The loss \(\eta>0\) is a fixed structural loss; constants depending on the fixed integers \(n_v\) affect polynomial prefactors, not this rate. Long fillings make the actual filled critical action arbitrarily close to \(F_0\), so it can be arranged above \(F_0-\eta/2\).

The remaining local comparison has a precise form. Replace the moving bare tensors by their complete tensors using the exponential regular-window alias estimate, and replace every filled circle tensor by (39). The only residual meridian dependence, besides the exact scalars (41), is the internal-edge factor
\[
 \gamma_N(s)\frac{H_N(s)}{W_{k}(s)}.
 \tag{51}
\]
Its canonical analytic wire continuation is
\[
 \gamma_N(s)
 \frac{G_N(Nx)^2}{G_N(Nx-s)G_N(Nx+s)}
       =1+O_R(N^{-1})
 \tag{52}
\]
uniformly on a fixed complex regular wire neighborhood. Thus it is a holomorphic amplitude perturbation, with no change to the selected action.

A whole filled profile now requires transporting this analytic amplitude through the original finite primitive wire window and its selected complex saddle, with its endpoint currents. A pointwise \(O(N^{-1})\) comparison on the real grid is insufficient: the filled exponent is smaller than the complete positive exponent. The required comparison is instead an insertion-compatible complex-window saddle statement for the unchanged complete bare tensors and (52), while retaining the circle integrals jointly. The [grouped wire packet](actual_main_meridian_grouped_wire_packet.md) constructs that finite window, and the [joint filling transform](actual_main_meridian_joint_filling_transform.md) keeps all circle charges until they have been compared at the same joint critical point. Selecting (39) separately at each circle before that comparison would not justify independently unequal long powers. The action match (47), the nonzero local amplitudes, and the exponentially accurate physical-grid comparison supply its local inputs. The original strict-source packet supplies the marked branch and the undeformed nonzero critical point. The compatibility of the actual finite wire contour and its holomorphic amplitude insertions must be stated explicitly before deducing a whole filled lower bound.

With the finite-window and joint-charge interfaces supplied by those companion proofs, the main cut contributes exactly one \(H_N(s)\), the framing ratio remains explicit, and the nonzero critical action is the knot-complement volume by Section 6. The [filled-volume theorem](actual_main_meridian_filled_volume.md) states that conclusion with its source and knot hypotheses. A norm upper bound alone would not supply the required nonzero saddle.
