# Fixed-carrier twist differences and their exact exterior correction

Private written proof, 15 November 2026.

The second-meridian-normal recovery has an exact relation to signed
twist powers. The relation retains one fixed half-twist parity:
the powers are \(\epsilon-2p\), with \(\epsilon\in\{-1,0,1\}\) fixed and
\(p\in\mathbb Z\). It supplies normal observations of the retained
boundary state. It does not identify those observations with changing
an arbitrary internal filling while leaving its exterior unrecorded.

The placement issue has an explicit source term. Restoring the actual
exterior introduces a commutator with the transported Casimir. Already
one original turn makes that term nonzero at completeness. Thus the
normal recovery does not by itself give a coefficient-ideal certificate
for the original complete filling family.

## 1. Actual operators and the fixed carrier

Use the coordinates and normalization of
[second-normal boundary recovery](research_second_meridian_normal_boundary_observability.md):
\(N\ge2\), \(d=N-1\), \(q=e^{\pi i/N}\), \(M=q^s\),
\(\ell=\mathbf e_d^T\), and
\[
\begin{split}
 (L_s)_{jj}&=c_j=2\cos((2j+1)\pi/N),\\
 (L_s)_{j-1,j}&=-4\sin((j-s)\pi/N)\sin((j+s)\pi/N),\\
 (L_s)_{d,0}&=\beta_s=(-1)^d4\sin^2(\pi s/N).
\end{split}                                                     \tag{1}
\]
The retained actual turn has coefficient matrix
\[
 \mathcal U_s=\frac{q^{-s^2/2}}{H_N(s)}
       J\,\operatorname{diag}(W_0(s),\ldots,W_d(s)),\qquad
 H_N(s)=\frac{\sin\pi s}{N\sin(\pi s/N)}.
 \tag{2}
\]
Here \(J\) is coefficient reversal and \(W_j\) are the paired sine
products in the cited note. The physical mixed-order carrier in the
[turn source](actual_main_meridian_turn_comparison.md) is retained
in this coefficient convention. In particular
\(\mathcal U_0=J\).

Let \(r_s(z)\), of degree less than \(N\), be the canonical polynomial
of the actual same-color positive crossing, with its Cartan scalar.
It is holomorphic near \(s=0\), at fixed \(N\). Indeed the actual
crossing matrix is holomorphic, and the full moment pairing of the
[physical compiler](actual_main_meridian_newton_compiler.md),
equations (16f)--(20), has a unit determinant at completeness.
Solving that finite pairing recovers holomorphic canonical coefficients.
This is a local assertion near completeness, not across every
ordinary-color resonance.

Let \(M_s^{\mathrm{mult}}\) denote multiplication by this crossing
in the input polynomial coordinates. The exact turn functional
calculus gives
\[
 B_s:=r_s(L_s)
      =\mathcal U_s M_s^{\mathrm{mult}}\mathcal U_s^{-1}.
 \tag{3}
\]
Thus \(B_s\) is an actual transported boundary operator.
It and \(r_s(c_0)\) are invertible near zero: the first is a conjugate
of an actual crossing, and the second has value
\(\kappa=q^{d^2/2}\ne0\) at zero.

Set
\[
\begin{split}
 a_s&=r_s(c_0),&
 h_s(z)&=\frac{r_s(z)-a_s}{z-c_0},\\
 T_s&=B_s^{-2},&
 \tau_s&=a_s^{-2},\\
 K_s&=-h_s(L_s)(B_s+a_sI)a_s^{-2}B_s^{-2}.
\end{split}                                                     \tag{4}
\]
The quotient \(h_s\) is a polynomial, with its removable value at
\(c_0\). All entries in (4) are known finite boundary operators or
known scalars; no unknown knot invariant is divided out.
Direct factorization gives
\[
                   T_s-\tau_sI=(L_s-c_0I)K_s.             \tag{5}
\]
All factors on the right commute with \(L_s\).

For an integer \(p\), define the finite Laurent polynomial
\[
 D_p(X,\tau)=\frac{X^p-\tau^p}{X-\tau},\qquad D_0=0.
 \tag{6}
\]
For \(p>0\) this is
\(\sum_{b=0}^{p-1}X^{p-1-b}\tau^b\); for \(p=-m<0\) it is
\(-\sum_{b=0}^{m-1}X^{-1-b}\tau^{b-m}\).
Equation (6) therefore needs neither spectral separation nor division
by \(T_s-\tau_sI\).

## 2. The exact normal difference in the retained row

Let \(u_s\) be any holomorphic actual boundary coefficient vector.
Keep \(\epsilon\) fixed and put
\[
 v_s=B_s^\epsilon u_s,\qquad
 Z_p(s)=\ell T_s^p v_s
       =\ell B_s^{\epsilon-2p}u_s .
 \tag{7}
\]
These are coefficient observations in the specified adapter.
The primitive physical cut contributes \(H_N(s)\); the turn scalars
and any remaining typed carrier are as in (2). They must be restored
before calling an intermediate coefficient observation a closed
invariant.

**Proposition 1.** For every fixed signed integer \(p\),
\[
 \boxed{\quad
 Z_p(s)-\tau_s^p Z_0(s)
   =\beta_s\,\mathbf e_0^T K_sD_p(T_s,\tau_s)v_s .
 \quad}                                                        \tag{8}
\]
Consequently
\[
 \boxed{\quad
 \left.\partial_s^2\bigl(Z_p-\tau_s^pZ_0\bigr)\right|_0
  =\frac{(-1)^d8\pi^2}{N^2}\,
       \mathbf e_0^TK_0D_p(T_0,\tau_0)B_0^\epsilon u_0 .
 \quad}                                                        \tag{9}
\]

**Proof.** The exact last row of (1) is
\(\ell(L_s-c_0I)=\beta_s\mathbf e_0^T\).
Apply this to (5) and
\(T_s^p-\tau_s^pI=(T_s-\tau_sI)D_p(T_s,\tau_s)\).
This proves (8), including negative powers.
Since \(\beta_0=\beta'_0=0\) and
\(\beta''_0=(-1)^d8\pi^2/N^2\), two derivatives leave no derivative
of \(u_s\), \(B_s\), \(K_s\), or \(D_p\). This proves (9).
\(\square\)

A common known scalar \(g_s\), holomorphic and nonzero at zero,
multiplies the right side of (9) by \(g_0\).
If original framing gives different known scalar units \(g_{p,s}\),
the exact comparison is made between
\(g_{p,s}^{-1}\mathcal Z_p\) and
\(\tau_s^p g_{0,s}^{-1}\mathcal Z_0\), where
\(\mathcal Z_p=g_{p,s}Z_p\).
This records the original scalar normalization; it does not silently
differentiate a differently normalized invariant.

At completeness the observations (7) themselves obey
\[
               Z_p(0)=\tau_0^p Z_0(0).                  \tag{10}
\]
Indeed \(\ell L_0=c_0\ell\), hence
\(\ell B_0^n=a_0^n\ell\) for every integer \(n\).
The extra information in (9) is therefore normal information.
The complete scalars (7) are not the general nontrivial filling family.

There is also a precise finite-level span statement. Write
\[
 \mathcal A_N=\mathbb C[z]/P_N(z),\qquad
 t(z)=r_0(z)^{-2}\ \text{in }\mathcal A_N,\qquad
 \mathcal B_N=\mathbb C[t]\subseteq\mathcal A_N .
 \tag{11}
\]
Here \(P_N(z)=2\mathrm T_N(z/2)+2\), with \(\mathrm T_N\) the
Chebyshev polynomial of the first kind.
The normal rows in (9), as \(p\) varies, span exactly
\(\mathbf e_0^TK_0\mathcal B_N(L_0)B_0^\epsilon\).
This follows because the \(D_p(X,\tau_0)\), \(p=1,2,\ldots\),
have successive degrees with leading coefficient one.
Multiplication by \(K_0\) is injective on \(\mathcal B_N\).
At a physical node where \(t(c)\ne t(c_0)\), its value
\((t(c)-t(c_0))/(c-c_0)\) is nonzero.
At \(c_0\) its value is \(t'(c_0)\ne0\), since the full crossing
has a nonzero logarithmic first normal there.
That length-two channel detects both coordinates of the entire
\(t(c_0)\) block in \(\mathcal B_N\), even if other physical nodes
have the same full-twist value. The analogous nonzero-channel
argument detects every other block. The full Hermite decomposition
therefore proves injectivity.

The first-coordinate row is cyclic for \(L_0\), by its nonzero
upper-bidiagonal entries, and \(B_0^\epsilon\) is invertible.
Thus the dimension of this span is exactly \(\dim\mathcal B_N\).
The archived [parity-preserving twist tomography](research_original_twist_observation_tomography.md),
§§2--4, supplies its spectral grouping: at odd prime levels it is
\(N\), whereas full-twist collisions can make it smaller at composite
levels. The first \(N\) positive values of \(p\) suffice at odd primes.
That is an \(N\)-dependent window, not a fixed finite list of fillings.
No new all-level interpolation assertion is being substituted for the
archived full Hermite one.

## 3. Restoring the actual exterior

Let \(E_s\) be the retained holomorphic exterior matrix in these
coefficient charts, and define
\[
                    Z_p^E(s)=\ell E_sT_s^p v_s .
 \tag{12}
\]
For an actual tangle compiler all its physical turns, multiplication
maps, carriers and closing maps remain in \(E_s\) or in the explicitly
recorded scalar factors. Merely absorbing \(E_s\) into \(u_s\) would
change the order of the boundary operation.

**Proposition 2.** The source-exact replacement for (8) is
\[
\boxed{\begin{split}
 Z_p^E-\tau_s^pZ_0^E
   ={}&\beta_s\mathbf e_0^TE_sK_sD_p(T_s,\tau_s)v_s\\
      &+\ell[E_s,L_s]K_sD_p(T_s,\tau_s)v_s .
\end{split}}                                                   \tag{13}
\]

**Proof.** Insert (5)--(6) in the difference in (12), then use
\[
 E_s(L_s-c_0I)
       =(L_s-c_0I)E_s+[E_s,L_s].
\]
The last-row identity proves (13). No commutation of the actual
exterior with the transported Casimir was assumed. \(\square\)

The second line of (13) is present for an original turn. At zero
\(E_0=J\), and (1) gives, including \(N=2\),
\[
 \boxed{\qquad
       \ell[J,L_0]=-4\sin^2(\pi/N)\,\mathbf e_1^T\ne0 .
 \qquad}                                                       \tag{14}
\]
Indeed \(\ell J=\mathbf e_0^T\),
\(\mathbf e_0^TL_0=c_0\mathbf e_0^T
-4\sin^2(\pi/N)\mathbf e_1^T\), and
\(\ell L_0J=c_0\mathbf e_0^T\).

This occurs in the ordinary filling placement itself. If \(f_s\) is
the input coefficient vector before the turn, take
\[
 u_s=\mathcal U_sf_s,\qquad E_s=\mathcal U_s^{-1}.
\]
Equations (3) and (12) then give exactly
\[
 Z_p^E(s)
     =\ell(M_s^{\mathrm{mult}})^{\epsilon-2p}f_s .
 \tag{15}
\]
This is the usual coefficient closing of the actual crossing-power
family, with its fixed carrier. Multiplication by the primitive cut
and known framing factors restores the physical closing, as above.
At zero, (15) is the original
\(\phi_N(R_N^{\epsilon-2p}f_0)\).
The exterior \(\mathcal U_s^{-1}\) cannot be omitted: its value is
the very turn in (14). Additional actual exterior pieces remain
additional factors in (12), rather than disappearing from (13).

Consequently the clean second derivative in (9) does not recover
the state from the scalar family (15). For that family one must
also differentiate the second line of (13). Its zeroth-order term
need not vanish, and its second derivative can contain derivatives
of the boundary state.

## 4. Consequence for an all-order filling coefficient ideal

Equations (8) and (13) hold at every fixed level and for each fixed
integer \(p\), before asymptotics. They are the precise link between
the new normal observations and actual boundary twist operations.
They establish neither a selected geometric expansion nor an
identification of its integration cycle.

Vanishing of every geometric coefficient of the original family
(15) cannot be inserted into (9): the omitted exterior term in
(13) is an actual source term. Even when the retained row (7) is
the intended observation, recovering a full arbitrary boundary
vector uses a number of powers that grows with \(N\), and uses
meridian derivatives rather than only the complete scalar.
Pointwise asymptotics for each fixed filling give no uniform
asymptotic statement for that growing window.

Thus a finite coefficient-ideal certificate would still need a
source-preserving finite geometric quotient on which the actual
exterior correction and the normal observations have a proved
all-order interpretation. The identities here neither construct
that quotient nor show that its original state is nonzero.
They rule out deleting the exterior while attempting that
construction, and provide the exact correction that must be kept.

## Direct written sources

- Second-normal boundary recovery: full matrix, row identity,
  normal normalization, and physical closing qualifications.
  SHA-256: e6aea663bac9cf1ed690f838c63977f010e4f9fd22d611958a273e2481ef24f8.
- Actual moving-meridian turn: equations (29), (34)--(35), and the
  typed orientation table.
  SHA-256: 9a4e617838bbeebd640615cd3a6f0178486d60f1a3ee0c8b8f620dd31ed4ffec.
- Actual meridian compiler: equations (16f)--(21), the integral
  centralizer, carrier, and primitive cut.
  SHA-256: 567b13019bf0fb2a7120d4139b9da78ebc481dee8ad7af30e2722a20b9e6506f.
- Original twist-observation tomography: §§2--4, including the
  fixed-parity reconstruction and composite-level collisions.
  SHA-256: 6885ad1b82b8f67ddda497f969337a9230b17925fd88b4326b0152dfdc738a1c.

Only written reasoning and text reads were used. No mathematical
execution, numerical evidence, tests, compilation, or frozen-source
edits entered this deduction.
